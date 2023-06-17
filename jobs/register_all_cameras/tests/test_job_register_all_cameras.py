import main as register_all_cameras
from main import zlm_server_cfg
from grpc_gen_code.cctv_crud_pb2 import (
    ListApplicationResponse,
    ApplicationFullData,
    ListMediaChannelsResponse,
    MediaChannelsRequest,
    CameraFullData
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
    mocker.patch('main.cctv_crud_stub.GetCameraByUid',
                    return_value=CameraFullData(
                        camera_uid="shouldNotAffectOutput",
                        camera_info="{\"detail\": \"shouldNotAffectOutput\"}",
                        is_enabled=True,
                        name="shouldNotAffectOutput",
                        raw_input_url="rtsp://cam_url/"
                    )
                )

    result = register_all_cameras.get_cameras()
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
            "raw_input_url": "rtsp://cam_url/",
            "app_type_id": 1
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
            "raw_input_url": "rtsp://cam_url/",
            "app_type_id": 2
        }

def test_check_cam_exist(requests_mock):
    app_type = "streaming"
    camera_uid = "cameraUid1"
    host = zlm_server_cfg['general']['mediaserverid']
    zlm_secret = zlm_server_cfg['api']['secret']
    zlm_vhost = "__defaultVhost__" # this is the default value if general.enableVhost is false
    # cam exist, return True
    #http://zlm-serveryour_server_id/index/api/getMediaList?secret=035c73f7-bb6b-4889-a715-d9eb2d1925cc&vhost=__defaultVhost__&app=streaming&stream=cameraUid1
    requests_mock.get("http://zlm-server-{APPLICATION_HOST}/index/api/getMediaList?secret={SECRET}&vhost={VHOST}&app={APP}&stream={STREAM}".format(
        APPLICATION_HOST=host,
        SECRET=zlm_secret,
        VHOST=zlm_vhost,
        APP=app_type,
        STREAM=camera_uid
        )
        , json={
                "code" : 0,
                "data" : [
                {
                    "app" : "live",  # 应用名
                    "readerCount" : 0, # 本协议观看人数
                    "totalReaderCount" : 0, # 观看总人数，包括hls/rtsp/rtmp/http-flv/ws-flv
                    "schema" : "rtsp", # 协议
                    "stream" : "obs", # 流id
                    "originSock": {  # 客户端和服务器网络信息，可能为null类型
                            "identifier": "140241931428384",
                            "local_ip": "127.0.0.1",
                            "local_port": 1935,
                            "peer_ip": "127.0.0.1",
                            "peer_port": 50097
                        },
                    "originType": 1, # 产生源类型，包括 unknown = 0,rtmp_push=1,rtsp_push=2,rtp_push=3,pull=4,ffmpeg_pull=5,mp4_vod=6,device_chn=7
                    "originTypeStr": "MediaOriginType::rtmp_push",
                    "originUrl": "rtmp://127.0.0.1:1935/live/hks2", #产生源的url
                    "createStamp": 1602205811, #GMT unix系统时间戳，单位秒
                    "aliveSecond": 100, #存活时间，单位秒
                    "bytesSpeed": 12345, #数据产生速度，单位byte/s
                    "tracks" : [    # 音视频轨道
                        {
                        "channels" : 1, # 音频通道数
                        "codec_id" : 2, # H264 = 0, H265 = 1, AAC = 2, G711A = 3, G711U = 4
                        "codec_id_name" : "CodecAAC", # 编码类型名称 
                        "codec_type" : 1, # Video = 0, Audio = 1
                        "ready" : True, # 轨道是否准备就绪
                        "frames" : 1119, #累计接收帧数
                        "sample_bit" : 16, # 音频采样位数
                        "sample_rate" : 8000 # 音频采样率
                        },
                        {
                        "codec_id" : 0, # H264 = 0, H265 = 1, AAC = 2, G711A = 3, G711U = 4
                        "codec_id_name" : "CodecH264", # 编码类型名称  
                        "codec_type" : 0, # Video = 0, Audio = 1
                        "fps" : 59,  # 视频fps
                        "frames" : 1119, #累计接收帧数，不包含sei/aud/sps/pps等不能解码的帧
                        "gop_interval_ms" : 1993, #gop间隔时间，单位毫秒
                        "gop_size" : 60, #gop大小，单位帧数
                        "key_frames" : 21, #累计接收关键帧数
                        "height" : 720, # 视频高
                        "ready" : True,  # 轨道是否准备就绪
                        "width" : 1280 # 视频宽
                        }
                    ],
                    "vhost" : "__defaultVhost__" # 虚拟主机名
                }
                ]
                }
    )
    assert register_all_cameras.check_cam_exist(app_type,camera_uid) == True
    # cam not exist, return False
    requests_mock.get("http://zlm-server-{APPLICATION_HOST}/index/api/getMediaList?secret={SECRET}&vhost={VHOST}&app={APP}&stream={STREAM}".format(
        APPLICATION_HOST=host,
        SECRET=zlm_secret,
        VHOST=zlm_vhost,
        APP=app_type,
        STREAM=camera_uid
        ),
        json={
                "code" : 0,
                "data" : []
                }
    )
    assert register_all_cameras.check_cam_exist(app_type,camera_uid) == False
    # endpoint cannot be reached, raise exception
    requests_mock.get("http://zlm-server-{APPLICATION_HOST}/index/api/getMediaList?secret={SECRET}&vhost={VHOST}&app={APP}&stream={STREAM}".format(
        APPLICATION_HOST=host,
        SECRET=zlm_secret,
        VHOST=zlm_vhost,
        APP=app_type,
        STREAM=camera_uid
        ),
        exc=requests.exceptions.ConnectTimeout
    )
    with pytest.raises(Exception):
        register_all_cameras.check_cam_exist(app_type,camera_uid)
    # endpoint return error code, raise exception
    requests_mock.get("http://zlm-server-{APPLICATION_HOST}/index/api/getMediaList?secret={SECRET}&vhost={VHOST}&app={APP}&stream={STREAM}".format(
        APPLICATION_HOST=host,
        SECRET=zlm_secret,
        VHOST=zlm_vhost,
        APP=app_type,
        STREAM=camera_uid
        ),
        json={
                "code" : 1,
                "data" : []
                }
    )
    with pytest.raises(Exception):
        register_all_cameras.check_cam_exist(app_type,camera_uid)

def test_register_camera(requests_mock):
    app_type = "ptz"
    camera_uid = "hks2"
    raw_input_url = "rtsp://abc.com"
    app_type = "streaming"
    camera_uid = "cameraUid1"
    host = zlm_server_cfg['general']['mediaserverid']
    zlm_secret = zlm_server_cfg['api']['secret']
    zlm_vhost = "__defaultVhost__" # this is the default value if general.enableVhost is false

# http://zlm-server-your_server_id/index/api/addStreamProxy?secret=035c73f7-bb6b-4889-a715-d9eb2d1925cc&schema=rtsp&vhost=__defaultVhost__&app=streaming&stream=cameraUid1&dst_url=rtsp%3A%2F%2Fabc.com&enable_hls=1&enable_mp4=True&enable_rtsp=1
    # register success
    requests_mock.get("http://zlm-server-{APPLICATION_HOST}/index/api/addStreamProxy?secret={SECRET}&schema={SCHEMA}&vhost={VHOST}&app={APP}&stream={STREAM}&dst_url={URL}&enable_hls=1&enable_mp4=1&enable_rtsp=1".format(
        APPLICATION_HOST=host,
        SECRET=zlm_secret,
        SCHEMA="rtsp",
        VHOST=zlm_vhost,
        APP=app_type,
        STREAM=camera_uid,
        URL=raw_input_url
        ),
        json={
                "code" : 0,
                "data" : {
                    "key": "rtmp/__defaultVhost__/proxy/test/4AB43C9EABEB76AB443BB8260C8B2D12"
                }
            }
    )
    # no error raised
    register_all_cameras.register_camera(app_type,camera_uid,raw_input_url,is_recording=True)

    # register failed, raise exception
    requests_mock.get("http://zlm-server-{APPLICATION_HOST}/index/api/addStreamProxy?secret={SECRET}&vhost={VHOST}&app={APP}&stream={STREAM}&dst_url={URL}&enable_hls=1&enable_mp4=1&enable_rtsp=1".format(
        APPLICATION_HOST=host,
        SECRET=zlm_secret,
        VHOST=zlm_vhost,
        APP=app_type,
        STREAM=camera_uid,
        URL=raw_input_url
        ),
        json={
                "code" : 1,
                "data" : {
                    "key": "rtmp/__defaultVhost__/proxy/test/4AB43C9EABEB76AB443BB8260C8B2D12"
                }
            }
    )
    # error raised
    with pytest.raises(Exception):
        register_all_cameras.register_camera(app_type,camera_uid,raw_input_url,is_recording=True)
    
    # endpoint cannot be reached, raise exception
    requests_mock.get("http://zlm-server-{APPLICATION_HOST}/index/api/addStreamProxy?secret={SECRET}&vhost={VHOST}&app={APP}&stream={STREAM}&dst_url={URL}&enable_hls=1&enable_mp4=1&enable_rtsp=1".format(
        APPLICATION_HOST=host,
        SECRET=zlm_secret,
        VHOST=zlm_vhost,
        APP=app_type,
        STREAM=camera_uid,
        URL=raw_input_url
        ),
        exc=requests.exceptions.ConnectTimeout
    )

    with pytest.raises(Exception):
        register_all_cameras.register_camera(app_type,camera_uid,raw_input_url,is_recording=True)
