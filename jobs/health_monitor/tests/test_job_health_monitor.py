import main as health_monitor
from main import zlm_server_cfg
from grpc_gen_code.cctv_crud_pb2 import (
    ListApplicationResponse,
    ApplicationFullData,
    ListMediaChannelsResponse,
    MediaChannelsRequest,
    CameraFullData,
    AppTypeFullData
)
import requests
import pytest

def test_get_cameras(mocker):
    mocker.patch('main.cctv_crud_stub.ListApplicationByHost'
                    , return_value=ListApplicationResponse(
                        applications=[
                            {
                                'app_uid':"appUid1",
                                'group_id':"groupId1",
                                'application_info':"{\"detail\": \"applicationInfo1\"}",
                                'is_enabled':True,
                                'host':"host1",
                                'app_type_id':1
                            },
                            {
                                'app_uid':"appUid2",
                                'group_id':"groupId2",
                                'application_info':"{\"detail\": \"applicationInfo2\"}",
                                'is_enabled':True,
                                'host':"host2",
                                'app_type_id':2
                            },
                            {
                                "app_uid":"appUid3",
                                "group_id":"groupId3",
                                "application_info":"{\"detail\": \"applicationInfo3\"}",
                                "is_enabled":False,
                                "host":"host3",
                                "app_type_id":3
                            }
                        ],
                        success=True
                    )
                )
    mocker.patch('main.cctv_crud_stub.ListMediaChannelsByAppUid'
                    , side_effect=[
                        ListMediaChannelsResponse(
                            media_channels=[
                                {
                                    "app_uid":"appUid1",
                                    'media_channel_id':1,
                                    'media_channel_info':"{\"detail\": \"mediaChannelInfo1\"}",
                                    'camera_uid':"cameraUid1",
                                    'is_enabled':True,
                                    'is_recording':True
                                }
                            ],
                            success=True
                        ),
                        ListMediaChannelsResponse(
                            media_channels=[
                                {
                                    "app_uid":"appUid2",
                                    'media_channel_id':2,
                                    'media_channel_info':"{\"detail\": \"mediaChannelInfo2\"}",
                                    'camera_uid':"cameraUid2",
                                    'is_enabled':True,
                                    'is_recording':False
                                }
                            ],
                            success=True
                        ),
                        ListMediaChannelsResponse(
                            media_channels=[
                                {
                                    'app_uid':"appUid3",
                                    'media_channel_id':3,
                                    'media_channel_info':"{\"detail\": \"mediaChannelInfo3\"}",
                                    'camera_uid':"cameraUid3",
                                    'is_enabled':False,
                                    'is_recording':False
                                }
                            ],
                            success=True
                        )
                    ]
                )
    # mocker.patch('main.cctv_crud_stub.GetCameraByUid',
    #                 return_value=CameraFullData(
    #                     camera_uid="shouldNotAffectOutput",
    #                     camera_info="{\"detail\": \"shouldNotAffectOutput\"}",
    #                     is_enabled=True,
    #                     name="shouldNotAffectOutput",
    #                     raw_input_url="rtsp://cam_url/"
    #                 )
    #             )
    mocker.patch('main.cctv_crud_stub.GetAppTypeById',
                    side_effect=[
                        AppTypeFullData(
                        app_type_id=1,
                        app_type_info="{\"detail\": \"shouldNotAffectOutput\"}",
                        is_enabled=True,
                        name="apptype1"
                        ),
                        AppTypeFullData(
                        app_type_id=2,
                        app_type_info="{\"detail\": \"shouldNotAffectOutput\"}",
                        is_enabled=True,
                        name="apptype2"
                        )
                    ]
                )

    result = health_monitor.get_cameras()
    assert len(result) == 2
    assert result[0] == {
            "app_uid": "appUid1",
            "group_id": "groupId1",
            "application_info": "{\"detail\": \"applicationInfo1\"}",
            "is_enabled": True,
            "media_channel_id": 1,
            "media_channel_info": "{\"detail\": \"mediaChannelInfo1\"}",
            "camera_uid": "cameraUid1",
            "is_recording": True,
            "app_type": "apptype1",
            "host": "",
        }
    assert result[1] == {
            "app_uid": "appUid2",
            "group_id": "groupId2",
            "application_info": "{\"detail\": \"applicationInfo2\"}",
            "is_enabled": True,
            "media_channel_id": 2,
            "media_channel_info": "{\"detail\": \"mediaChannelInfo2\"}",
            "camera_uid": "cameraUid2",
            "is_recording": False,
            "host": "host2",
            "app_type": "apptype2"
        }

def _test_health_monitor(mocker):
    mocker.patch('main.get_cameras', return_value=[
                    {
                        "app_uid": "aiohe",
                        "group_id": "9cb5c1d8-31be-44a5-b8d8-32bb6c3d57a4",
                        "application_info": {},
                        "host": "12345",
                        "app_type": "streaming",
                        "media_channel_id": 1,
                        "media_channel_info": {},
                        "camera_uid": "boi9mnahgn",
                        "is_enabled": True,
                        "is_recording": True,
                    }
                ]
            )
    pass

def test_check_health(mocker):
    mocker.patch('main.resolve_url', return_value="rtmp://ns8.indexforce.com/home/mystream")
    assert health_monitor.check_health("rtmp://ns8.indexforce.com/home/mystream",
                                    "test",
                                    "test",
                                    "test"
                                    ) == True
