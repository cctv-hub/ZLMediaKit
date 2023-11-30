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
import asyncio

pytest_plugins = ('anyio')

@pytest.fixture
def anyio_backend():
    return 'asyncio'

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
            "host": "host1",
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

def test_check_cam_health_tasks(mocker):
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
    mocker.patch('main.resolve_url', return_value="rtmp://ns8.indexforce.com/home/mystream")
    mocker.patch('main.write_health_log', return_value=True)
    no_error = health_monitor.check_cam_health_tasks("12345", "streaming", "boi9mnahgn", 1)
    assert no_error

def test_check_health(mocker):
    mocker.patch('main.resolve_url', return_value="rtmp://ns8.indexforce.com/home/mystream")
    assert health_monitor.check_health("rtmp://ns8.indexforce.com/home/mystream",
                                    "test",
                                    "test",
                                    "test"
                                    ) == True

def test_check_health_fail(mocker):
    mocker.patch('main.resolve_url', return_value="rtmp://localhost/whatever")
    mocker.patch('main.requests.get', side_effect=requests.exceptions.ConnectionError)
    assert health_monitor.check_health("rtmp://localhost/whatever",
                                    "test",
                                    "test",
                                    "test"
                                    ) == False

@pytest.mark.anyio
async def test_acheck_health(mocker):
    mocker.patch('main.resolve_url', return_value="rtmp://ns8.indexforce.com/home/mystream")
    r = await health_monitor.acheck_health("rtmp://ns8.indexforce.com/home/mystream",
                                    "test",
                                    "test",
                                    "test"
                                    ) == True
    assert r == True

@pytest.mark.anyio
async def test_acheck_cam_health_tasks(mocker):
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
    mocker.patch('main.resolve_url', return_value="rtmp://ns8.indexforce.com/home/mystream")
    mocker.patch('main.write_health_log', return_value=True)
    no_error = await health_monitor.acheck_cam_health_tasks("12345", "streaming", "boi9mnahgn", 1)
    assert no_error

def test_amain(mocker):
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
    mocker.patch('main.resolve_url', return_value="rtmp://ns8.indexforce.com/home/mystream")
    mocker.patch('main.write_health_log', return_value=True)
    health_monitor.amain()

def test_main(mocker):
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
    mocker.patch('main.resolve_url', return_value="rtmp://ns8.indexforce.com/home/mystream")
    mocker.patch('main.write_health_log', return_value=True)
    health_monitor.main()