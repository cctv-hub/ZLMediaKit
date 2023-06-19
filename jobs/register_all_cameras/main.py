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
    GetCameraByUidRequest,
    GetAppTypeByIdRequest
)
import time
import grpc

DEPLOY_MODE = os.environ.get('DEPLOY_MODE', 'docker')
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
                    cam_metadata = cctv_crud_stub.GetCameraByUid(GetCameraByUidRequest(
                        camera_uid=mc.camera_uid
                    )
                    )
                    app_type = cctv_crud_stub.GetAppTypeById(GetAppTypeByIdRequest(
                        app_type_id=app.app_type_id
                    )
                    ).name
                    full_list_of_cameras.append(
                        {
                            "app_uid": app.app_uid,
                            "group_id": app.group_id,
                            "application_info": app.application_info,
                            "app_type": app_type,
                            "media_channel_id": mc.media_channel_id,
                            "media_channel_info": mc.media_channel_info,
                            "camera_uid": mc.camera_uid,
                            "is_enabled": mc.is_enabled,
                            "is_recording": mc.is_recording,
                            "raw_input_url": cam_metadata.raw_input_url,
                        }
                    )
    logger.debug(f"{full_list_of_cameras=}")
    return full_list_of_cameras

def check_cam_exist(app_type, camera_uid):
    response = requests.get(f"http://{_resolve_host(host)}/index/api/getMediaList?secret={zlm_secret}&vhost={zlm_vhost}&app={app_type}&stream={camera_uid}")
    if response.status_code != 200:
        logger.error(f"Error when checking camera {camera_uid} on app {app_type}")
        raise Exception(f"Error when checking camera {camera_uid} on app {app_type}")
    else:
        response = response.json()
        if response["code"] == 0:
            logger.info(f"getMediaList for camera {camera_uid} on app {app_type} successfully")
            if len(response.get("data",[])) == 0:
                return False
            else:
                return True
        else:
            raise Exception(f"Error when checking camera {camera_uid} on app {app_type}")

def register_camera(app_type, camera_uid, raw_input_url,is_recording):
    schema = raw_input_url.split("://")[0]
    response = requests.get(f"http://{_resolve_host(host)}/index/api/addStreamProxy",
                             params={
                                    "secret": zlm_secret,
                                    "schema": schema,
                                    "vhost": zlm_vhost,
                                    "app": app_type,
                                    "stream": camera_uid,
                                    "url": raw_input_url,
                                    "enable_hls": 1,
                                    "enable_mp4": int(is_recording),
                                    "enable_rtsp": 1
                                })
    if response.status_code != 200:
        logger.error(f"Error when registering camera {camera_uid} on app {app_type}")
        raise Exception(f"Error when registering camera {camera_uid} on app {app_type}")
    else:
        response = response.json()
        if response["code"] == 0:
            logger.info(f"Camera {camera_uid} on app {app_type} registered successfully")
            return response['data']['key']
        else:
            raise Exception(f"Error when registering camera {camera_uid} on app {app_type}")

def main():
    # get cam list from db
    full_list_of_cameras = get_cameras()
    while len(full_list_of_cameras) > 0:
        cam = full_list_of_cameras.pop()
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
            # if error, put back to the list
            full_list_of_cameras.insert(0, cam)
        # wait for 5 seconds
        time.sleep(5)
        
if __name__ == "__main__":
    main()