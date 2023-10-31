import requests
import yaml
import configparser
import os
from loguru import logger
from grpc_gen_code.business_logic_pb2_grpc import bizLogicStub
from grpc_gen_code.cctv_crud_pb2_grpc import CctvCrudStub
from grpc_gen_code.cctv_crud_pb2 import (
    ListApplicationByHostRequest,
    MediaChannelsRequest,
    CreateMediaChannelHealthLogRequest,
    GetAppTypeByIdRequest
)
import time
import grpc
import cv2

DEPLOY_MODE = os.environ.get('DEPLOY_MODE', 'docker')
COOLDOWN_SECOND = int(os.environ.get('COOLDOWN_SECOND', "5"))
with open("conf/config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

channel = grpc.insecure_channel(
    f'{cfg["zlm-load-balancer"]["host"]}:{cfg["zlm-load-balancer"]["port"]}'
)
biz_logic_stub = bizLogicStub(channel)
cctv_crud_stub = CctvCrudStub(channel)

zlm_server_cfg = configparser.ConfigParser()
zlm_server_cfg.read("conf/config.ini")
host = zlm_server_cfg['general']['mediaserverid']
zlm_secret = zlm_server_cfg['api']['secret']
zlm_vhost = "__defaultVhost__" # this is the default value if general.enableVhost is false

def _resolve_host(h):
    if DEPLOY_MODE == "docker":
        return "zlm-server-" + h
    else:
        return h

def get_cameras():
    # Get the list of cameras from db
    full_list_of_cameras = []
    # call ListApplicationByHost -> ListMediaChannelsByAppUid from zlm-load-balancer
    list_of_app = cctv_crud_stub.ListApplicationByHost(ListApplicationByHostRequest(
        host = host
        )
    ).applications
    for app in list_of_app:
        if app.is_enabled:
            list_of_mc = cctv_crud_stub.ListMediaChannelsByAppUid(MediaChannelsRequest(
                app_uid=app.app_uid
                )
            ).media_channels
            for mc in list_of_mc:
                if mc.is_enabled:
                    app_type = cctv_crud_stub.GetAppTypeById(GetAppTypeByIdRequest(
                        app_type_id=app.app_type_id
                    )
                    ).name
                    full_list_of_cameras.append(
                        {
                            "app_uid": app.app_uid,
                            "group_id": app.group_id,
                            "application_info": app.application_info,
                            "host": app.host,
                            "app_type": app_type,
                            "media_channel_id": mc.media_channel_id,
                            "media_channel_info": mc.media_channel_info,
                            "camera_uid": mc.camera_uid,
                            "is_enabled": mc.is_enabled,
                            "is_recording": mc.is_recording,
                        }
                    )
    logger.debug(f"{full_list_of_cameras=}")
    return full_list_of_cameras

def resolve_server_dns(zlm_server_id, is_internal=True):
    if is_internal:
        deploy_mode = os.environ.get("DEPLOY_MODE", "docker")
        if deploy_mode == "k8s":
            # k8s
            ZLMediaKit_URL = f"{zlm_server_id}.cctv-hub.svc.cluster.local"
        else:
            # docker
            ZLMediaKit_URL = f"zlm-server-{zlm_server_id}"
        return ZLMediaKit_URL
    else:
        # external
        return f"{cfg['root_domain']}"

def check_health(host, app_type_name, camera_uid, mode):
    if mode == "rtsp":
        output = f"http://{resolve_server_dns(host,is_internal=True)}/{app_type_name}/{camera_uid}"
    elif mode == "hls":
        output = f"http://{resolve_server_dns(host,is_internal=True)}/{app_type_name}/{camera_uid}/hls.m3u8"
    with cv2.VideoCapture(output) as cap:
        return cap.isOpened()

def write_health_log():
    # call CreateMediaChannelHealthLog from zlm-load-balancer
    pass
def main():
    # get cam list from db
    while True:
        full_list_of_cameras = get_cameras()
        for cam in full_list_of_cameras:
            try:
                # check if cam exist on zlm
                if check_cam_exist(cam["app_type"], cam["camera_uid"]):
                    # if exist, do nothing
                    logger.info(f"Camera {cam['camera_uid']} on app {cam['app_uid']} already exist on zlm")
                else:
                    # if not exist, register
                    register_camera(cam["app_type"], cam["camera_uid"], cam["raw_input_url"], cam["is_recording"])
            except Exception as e:
                logger.error(f"Error when registering camera {cam['camera_uid']} on app {cam['app_uid']}: {e}")

        # wait for X seconds
        time.sleep(COOLDOWN_SECOND)
        
if __name__ == "__main__":
    main()