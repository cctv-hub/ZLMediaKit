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

def resolve_url(zlm_server_id, app_type_name, camera_uid, is_internal, mode):
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
    
    if mode == "rtsp":
        output = f"http://{resolve_server_dns(zlm_server_id,is_internal=is_internal)}/{app_type_name}/{camera_uid}"
    elif mode == "hls":
        output = f"http://{resolve_server_dns(zlm_server_id,is_internal=is_internal)}/{app_type_name}/{camera_uid}/hls.m3u8"
    else:
        raise ValueError(f"Invalid mode: {mode}")
    return output

def check_health(host, app_type_name, camera_uid, mode) -> bool:
    output = resolve_url(host, app_type_name, camera_uid, is_internal=True, mode=mode)
    with cv2.VideoCapture(output) as cap:
        return cap.isOpened()

def write_health_log(media_channel_id,snapshot_health,rtsp_out_health,hls_out_health):
    # call CreateMediaChannelHealthLog from zlm-load-balancer
    try:
        response = cctv_crud_stub.CreateMediaChannelHealthLog(CreateMediaChannelHealthLogRequest(
            media_channel_id = media_channel_id,
            snapshot_health = snapshot_health,
            rtsp_out_health = rtsp_out_health,
            hls_out_health = hls_out_health,
            )
        )
        logger.debug(f"CreateMediaChannelHealthLog response: {response}")
    except Exception as e:
        logger.error(f"Error when calling CreateMediaChannelHealthLog: {e}")

def main():
    # get cam list from db
    while True:
        full_list_of_cameras = get_cameras()
        for cam in full_list_of_cameras:
            try:
                # check rtsp health
                rtsp_out_health = check_health(cam["host"], cam["app_type"], cam["camera_uid"], "rtsp")
                # check hls health
                hls_out_health = check_health(cam["host"], cam["app_type"], cam["camera_uid"], "hls")
                # check snapshot health
                snapshot_health = hls_out_health # assume snapshot health is the same as hls health
                # write health log
                write_health_log(cam["media_channel_id"],snapshot_health,rtsp_out_health,hls_out_health)
            except Exception as e:
                logger.error(f"Error when checking health on {cam=}: {e}")
        # wait for X seconds
        time.sleep(COOLDOWN_SECOND)
        
if __name__ == "__main__":
    main()