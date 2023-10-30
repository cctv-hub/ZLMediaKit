from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteAppByCameraUidRequest(_message.Message):
    __slots__ = ["app_type_id", "camera_uid"]
    APP_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    app_type_id: int
    camera_uid: str
    def __init__(self, camera_uid: _Optional[str] = ..., app_type_id: _Optional[int] = ...) -> None: ...

class DeleteAppByCameraUidResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class DeleteCameraByUidRequest(_message.Message):
    __slots__ = ["camera_uid"]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    camera_uid: str
    def __init__(self, camera_uid: _Optional[str] = ...) -> None: ...

class DeleteCameraByUidResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetCameraByGroupAndNameRequest(_message.Message):
    __slots__ = ["group_id", "name"]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    name: str
    def __init__(self, group_id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetCameraByUidRequest(_message.Message):
    __slots__ = ["camera_uid"]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    camera_uid: str
    def __init__(self, camera_uid: _Optional[str] = ...) -> None: ...

class GetCameraResponse(_message.Message):
    __slots__ = ["camera_brand", "camera_config_url", "camera_info", "camera_model", "camera_uid", "description", "group_id", "media_channel_data", "name", "parameter_distortion", "parameter_intrinsic_matrix", "parameter_position", "parameter_rotation", "raw_input_url", "router_brand", "router_config_url", "router_model"]
    CAMERA_BRAND_FIELD_NUMBER: _ClassVar[int]
    CAMERA_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_INFO_FIELD_NUMBER: _ClassVar[int]
    CAMERA_MODEL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_DATA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_DISTORTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_INTRINSIC_MATRIX_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_POSITION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_ROTATION_FIELD_NUMBER: _ClassVar[int]
    RAW_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_BRAND_FIELD_NUMBER: _ClassVar[int]
    ROUTER_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_MODEL_FIELD_NUMBER: _ClassVar[int]
    camera_brand: str
    camera_config_url: str
    camera_info: str
    camera_model: str
    camera_uid: str
    description: str
    group_id: str
    media_channel_data: _containers.RepeatedCompositeFieldContainer[MediaChannelOutputData]
    name: str
    parameter_distortion: _containers.RepeatedScalarFieldContainer[float]
    parameter_intrinsic_matrix: _containers.RepeatedScalarFieldContainer[float]
    parameter_position: _containers.RepeatedScalarFieldContainer[float]
    parameter_rotation: _containers.RepeatedScalarFieldContainer[float]
    raw_input_url: str
    router_brand: str
    router_config_url: str
    router_model: str
    def __init__(self, camera_uid: _Optional[str] = ..., group_id: _Optional[str] = ..., name: _Optional[str] = ..., camera_info: _Optional[str] = ..., description: _Optional[str] = ..., camera_brand: _Optional[str] = ..., camera_model: _Optional[str] = ..., camera_config_url: _Optional[str] = ..., router_brand: _Optional[str] = ..., router_model: _Optional[str] = ..., router_config_url: _Optional[str] = ..., parameter_intrinsic_matrix: _Optional[_Iterable[float]] = ..., parameter_position: _Optional[_Iterable[float]] = ..., parameter_rotation: _Optional[_Iterable[float]] = ..., parameter_distortion: _Optional[_Iterable[float]] = ..., raw_input_url: _Optional[str] = ..., media_channel_data: _Optional[_Iterable[_Union[MediaChannelOutputData, _Mapping]]] = ...) -> None: ...

class ListStreamingChannelsByGroupIdsRequest(_message.Message):
    __slots__ = ["group_ids"]
    GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    group_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, group_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListStreamingChannelsByGroupIdsResponse(_message.Message):
    __slots__ = ["channels"]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    channels: _containers.RepeatedCompositeFieldContainer[StreamingChannelForFrontend]
    def __init__(self, channels: _Optional[_Iterable[_Union[StreamingChannelForFrontend, _Mapping]]] = ...) -> None: ...

class MediaChannelInputData(_message.Message):
    __slots__ = ["app_type_id", "is_recording", "media_channel_info"]
    APP_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    IS_RECORDING_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_INFO_FIELD_NUMBER: _ClassVar[int]
    app_type_id: int
    is_recording: bool
    media_channel_info: str
    def __init__(self, app_type_id: _Optional[int] = ..., media_channel_info: _Optional[str] = ..., is_recording: bool = ...) -> None: ...

class MediaChannelOutputData(_message.Message):
    __slots__ = ["app_type_id", "app_uid", "is_recording", "media_channel_id", "media_channel_info"]
    APP_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    IS_RECORDING_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_INFO_FIELD_NUMBER: _ClassVar[int]
    app_type_id: int
    app_uid: str
    is_recording: bool
    media_channel_id: int
    media_channel_info: str
    def __init__(self, app_uid: _Optional[str] = ..., media_channel_id: _Optional[int] = ..., media_channel_info: _Optional[str] = ..., app_type_id: _Optional[int] = ..., is_recording: bool = ...) -> None: ...

class RegisterAppByCameraUidRequest(_message.Message):
    __slots__ = ["camera_uid", "group_id", "media_channel_config"]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    camera_uid: str
    group_id: str
    media_channel_config: MediaChannelInputData
    def __init__(self, camera_uid: _Optional[str] = ..., group_id: _Optional[str] = ..., media_channel_config: _Optional[_Union[MediaChannelInputData, _Mapping]] = ...) -> None: ...

class RegisterAppByCameraUidResponse(_message.Message):
    __slots__ = ["media_channel_data", "success"]
    MEDIA_CHANNEL_DATA_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    media_channel_data: MediaChannelOutputData
    success: bool
    def __init__(self, media_channel_data: _Optional[_Union[MediaChannelOutputData, _Mapping]] = ..., success: bool = ...) -> None: ...

class RegisterCameraRequest(_message.Message):
    __slots__ = ["camera_brand", "camera_config_url", "camera_info", "camera_model", "description", "group_id", "media_channel_config", "name", "parameter_distortion", "parameter_intrinsic_matrix", "parameter_position", "parameter_rotation", "raw_input_url", "router_brand", "router_config_url", "router_model"]
    CAMERA_BRAND_FIELD_NUMBER: _ClassVar[int]
    CAMERA_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_INFO_FIELD_NUMBER: _ClassVar[int]
    CAMERA_MODEL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_DISTORTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_INTRINSIC_MATRIX_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_POSITION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_ROTATION_FIELD_NUMBER: _ClassVar[int]
    RAW_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_BRAND_FIELD_NUMBER: _ClassVar[int]
    ROUTER_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_MODEL_FIELD_NUMBER: _ClassVar[int]
    camera_brand: str
    camera_config_url: str
    camera_info: str
    camera_model: str
    description: str
    group_id: str
    media_channel_config: _containers.RepeatedCompositeFieldContainer[MediaChannelInputData]
    name: str
    parameter_distortion: _containers.RepeatedScalarFieldContainer[float]
    parameter_intrinsic_matrix: _containers.RepeatedScalarFieldContainer[float]
    parameter_position: _containers.RepeatedScalarFieldContainer[float]
    parameter_rotation: _containers.RepeatedScalarFieldContainer[float]
    raw_input_url: str
    router_brand: str
    router_config_url: str
    router_model: str
    def __init__(self, group_id: _Optional[str] = ..., name: _Optional[str] = ..., camera_info: _Optional[str] = ..., description: _Optional[str] = ..., camera_brand: _Optional[str] = ..., camera_model: _Optional[str] = ..., camera_config_url: _Optional[str] = ..., router_brand: _Optional[str] = ..., router_model: _Optional[str] = ..., router_config_url: _Optional[str] = ..., parameter_intrinsic_matrix: _Optional[_Iterable[float]] = ..., parameter_position: _Optional[_Iterable[float]] = ..., parameter_rotation: _Optional[_Iterable[float]] = ..., parameter_distortion: _Optional[_Iterable[float]] = ..., raw_input_url: _Optional[str] = ..., media_channel_config: _Optional[_Iterable[_Union[MediaChannelInputData, _Mapping]]] = ...) -> None: ...

class RegisterCameraResponse(_message.Message):
    __slots__ = ["camera_uid", "media_channel_data", "success"]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_DATA_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    camera_uid: str
    media_channel_data: _containers.RepeatedCompositeFieldContainer[MediaChannelOutputData]
    success: bool
    def __init__(self, camera_uid: _Optional[str] = ..., media_channel_data: _Optional[_Iterable[_Union[MediaChannelOutputData, _Mapping]]] = ..., success: bool = ...) -> None: ...

class StreamingChannelForFrontend(_message.Message):
    __slots__ = ["app_uid", "camera_info", "camera_name", "camera_uid", "display_msg", "is_recording", "media_channel_id", "media_channel_info"]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    CAMERA_INFO_FIELD_NUMBER: _ClassVar[int]
    CAMERA_NAME_FIELD_NUMBER: _ClassVar[int]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MSG_FIELD_NUMBER: _ClassVar[int]
    IS_RECORDING_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_INFO_FIELD_NUMBER: _ClassVar[int]
    app_uid: str
    camera_info: str
    camera_name: str
    camera_uid: str
    display_msg: str
    is_recording: bool
    media_channel_id: int
    media_channel_info: str
    def __init__(self, media_channel_info: _Optional[str] = ..., media_channel_id: _Optional[int] = ..., display_msg: _Optional[str] = ..., camera_uid: _Optional[str] = ..., app_uid: _Optional[str] = ..., is_recording: bool = ..., camera_info: _Optional[str] = ..., camera_name: _Optional[str] = ...) -> None: ...

class UpdateCameraAppRequest(_message.Message):
    __slots__ = ["app_type_id", "camera_uid", "is_recording"]
    APP_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    IS_RECORDING_FIELD_NUMBER: _ClassVar[int]
    app_type_id: int
    camera_uid: str
    is_recording: bool
    def __init__(self, camera_uid: _Optional[str] = ..., app_type_id: _Optional[int] = ..., is_recording: bool = ...) -> None: ...

class UpdateCameraAppResponse(_message.Message):
    __slots__ = ["app_uid", "success"]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    app_uid: str
    success: bool
    def __init__(self, app_uid: _Optional[str] = ..., success: bool = ...) -> None: ...

class UpdateCameraMetadataRequest(_message.Message):
    __slots__ = ["camera_uid", "name"]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    camera_uid: str
    name: str
    def __init__(self, camera_uid: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateCameraMetadataResponse(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
