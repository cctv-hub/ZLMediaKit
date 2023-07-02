from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppTypeFullData(_message.Message):
    __slots__ = ["app_type_id", "app_type_info", "application_jsonschema", "channel_jsonschema", "created_at", "description", "is_enabled", "name", "updated_at"]
    APPLICATION_JSONSCHEMA_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_INFO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_JSONSCHEMA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    app_type_id: int
    app_type_info: str
    application_jsonschema: str
    channel_jsonschema: str
    created_at: _timestamp_pb2.Timestamp
    description: str
    is_enabled: bool
    name: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, app_type_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_enabled: bool = ..., app_type_info: _Optional[str] = ..., channel_jsonschema: _Optional[str] = ..., application_jsonschema: _Optional[str] = ...) -> None: ...

class AppTypeRequest(_message.Message):
    __slots__ = ["app_type_id", "app_type_info", "application_jsonschema", "channel_jsonschema", "description", "name"]
    APPLICATION_JSONSCHEMA_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_INFO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_JSONSCHEMA_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    app_type_id: int
    app_type_info: str
    application_jsonschema: str
    channel_jsonschema: str
    description: str
    name: str
    def __init__(self, app_type_id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., app_type_info: _Optional[str] = ..., channel_jsonschema: _Optional[str] = ..., application_jsonschema: _Optional[str] = ...) -> None: ...

class AppTypeResponse(_message.Message):
    __slots__ = ["app_type", "success"]
    APP_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    app_type: AppTypeFullData
    success: bool
    def __init__(self, app_type: _Optional[_Union[AppTypeFullData, _Mapping]] = ..., success: bool = ...) -> None: ...

class ApplicationFullData(_message.Message):
    __slots__ = ["app_type_id", "app_uid", "application_info", "created_at", "group_id", "host", "is_enabled", "updated_at"]
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    app_type_id: int
    app_uid: str
    application_info: str
    created_at: _timestamp_pb2.Timestamp
    group_id: str
    host: str
    is_enabled: bool
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, app_uid: _Optional[str] = ..., group_id: _Optional[str] = ..., host: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_enabled: bool = ..., application_info: _Optional[str] = ..., app_type_id: _Optional[int] = ...) -> None: ...

class ApplicationRequest(_message.Message):
    __slots__ = ["app_uid", "group_id", "host"]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    app_uid: str
    group_id: str
    host: str
    def __init__(self, app_uid: _Optional[str] = ..., group_id: _Optional[str] = ..., host: _Optional[str] = ...) -> None: ...

class ApplicationResponse(_message.Message):
    __slots__ = ["application", "success"]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    application: ApplicationFullData
    success: bool
    def __init__(self, application: _Optional[_Union[ApplicationFullData, _Mapping]] = ..., success: bool = ...) -> None: ...

class CameraFullData(_message.Message):
    __slots__ = ["camera_brand", "camera_config_url", "camera_info", "camera_model", "camera_uid", "created_at", "description", "is_enabled", "name", "parameter_distortion", "parameter_intrinsic_matrix", "parameter_position", "parameter_rotation", "raw_input_url", "router_brand", "router_config_url", "router_model", "updated_at"]
    CAMERA_BRAND_FIELD_NUMBER: _ClassVar[int]
    CAMERA_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_INFO_FIELD_NUMBER: _ClassVar[int]
    CAMERA_MODEL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_DISTORTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_INTRINSIC_MATRIX_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_POSITION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_ROTATION_FIELD_NUMBER: _ClassVar[int]
    RAW_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_BRAND_FIELD_NUMBER: _ClassVar[int]
    ROUTER_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_MODEL_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    camera_brand: str
    camera_config_url: str
    camera_info: str
    camera_model: str
    camera_uid: str
    created_at: _timestamp_pb2.Timestamp
    description: str
    is_enabled: bool
    name: str
    parameter_distortion: _containers.RepeatedScalarFieldContainer[float]
    parameter_intrinsic_matrix: _containers.RepeatedScalarFieldContainer[float]
    parameter_position: _containers.RepeatedScalarFieldContainer[float]
    parameter_rotation: _containers.RepeatedScalarFieldContainer[float]
    raw_input_url: str
    router_brand: str
    router_config_url: str
    router_model: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, camera_uid: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_enabled: bool = ..., camera_info: _Optional[str] = ..., raw_input_url: _Optional[str] = ..., description: _Optional[str] = ..., camera_brand: _Optional[str] = ..., camera_model: _Optional[str] = ..., camera_config_url: _Optional[str] = ..., router_brand: _Optional[str] = ..., router_model: _Optional[str] = ..., router_config_url: _Optional[str] = ..., parameter_intrinsic_matrix: _Optional[_Iterable[float]] = ..., parameter_position: _Optional[_Iterable[float]] = ..., parameter_rotation: _Optional[_Iterable[float]] = ..., parameter_distortion: _Optional[_Iterable[float]] = ...) -> None: ...

class CameraRequest(_message.Message):
    __slots__ = ["camera_uid", "group_id", "name"]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    camera_uid: str
    group_id: str
    name: str
    def __init__(self, camera_uid: _Optional[str] = ..., name: _Optional[str] = ..., group_id: _Optional[str] = ...) -> None: ...

class CameraResponse(_message.Message):
    __slots__ = ["camera", "success"]
    CAMERA_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    camera: CameraFullData
    success: bool
    def __init__(self, camera: _Optional[_Union[CameraFullData, _Mapping]] = ..., success: bool = ...) -> None: ...

class CreateAppTypeRequest(_message.Message):
    __slots__ = ["app_type_info", "application_jsonschema", "channel_jsonschema", "created_at", "description", "is_enabled", "name", "updated_at"]
    APPLICATION_JSONSCHEMA_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_INFO_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_JSONSCHEMA_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    app_type_info: str
    application_jsonschema: str
    channel_jsonschema: str
    created_at: _timestamp_pb2.Timestamp
    description: str
    is_enabled: bool
    name: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., description: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_enabled: bool = ..., app_type_info: _Optional[str] = ..., channel_jsonschema: _Optional[str] = ..., application_jsonschema: _Optional[str] = ...) -> None: ...

class CreateApplicationRequest(_message.Message):
    __slots__ = ["app_type_id", "app_uid", "application_info", "created_at", "group_id", "host", "is_enabled", "updated_at"]
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    APP_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    app_type_id: int
    app_uid: str
    application_info: str
    created_at: _timestamp_pb2.Timestamp
    group_id: str
    host: str
    is_enabled: bool
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, app_uid: _Optional[str] = ..., group_id: _Optional[str] = ..., host: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_enabled: bool = ..., application_info: _Optional[str] = ..., app_type_id: _Optional[int] = ...) -> None: ...

class CreateCameraRequest(_message.Message):
    __slots__ = ["camera_brand", "camera_config_url", "camera_info", "camera_model", "camera_uid", "created_at", "description", "group_id", "is_enabled", "name", "parameter_distortion", "parameter_intrinsic_matrix", "parameter_position", "parameter_rotation", "raw_input_url", "router_brand", "router_config_url", "router_model", "updated_at"]
    CAMERA_BRAND_FIELD_NUMBER: _ClassVar[int]
    CAMERA_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_INFO_FIELD_NUMBER: _ClassVar[int]
    CAMERA_MODEL_FIELD_NUMBER: _ClassVar[int]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_DISTORTION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_INTRINSIC_MATRIX_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_POSITION_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_ROTATION_FIELD_NUMBER: _ClassVar[int]
    RAW_INPUT_URL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_BRAND_FIELD_NUMBER: _ClassVar[int]
    ROUTER_CONFIG_URL_FIELD_NUMBER: _ClassVar[int]
    ROUTER_MODEL_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    camera_brand: str
    camera_config_url: str
    camera_info: str
    camera_model: str
    camera_uid: str
    created_at: _timestamp_pb2.Timestamp
    description: str
    group_id: str
    is_enabled: bool
    name: str
    parameter_distortion: _containers.RepeatedScalarFieldContainer[float]
    parameter_intrinsic_matrix: _containers.RepeatedScalarFieldContainer[float]
    parameter_position: _containers.RepeatedScalarFieldContainer[float]
    parameter_rotation: _containers.RepeatedScalarFieldContainer[float]
    raw_input_url: str
    router_brand: str
    router_config_url: str
    router_model: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, camera_uid: _Optional[str] = ..., name: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_enabled: bool = ..., camera_info: _Optional[str] = ..., raw_input_url: _Optional[str] = ..., group_id: _Optional[str] = ..., description: _Optional[str] = ..., camera_brand: _Optional[str] = ..., camera_model: _Optional[str] = ..., camera_config_url: _Optional[str] = ..., router_brand: _Optional[str] = ..., router_model: _Optional[str] = ..., router_config_url: _Optional[str] = ..., parameter_intrinsic_matrix: _Optional[_Iterable[float]] = ..., parameter_position: _Optional[_Iterable[float]] = ..., parameter_rotation: _Optional[_Iterable[float]] = ..., parameter_distortion: _Optional[_Iterable[float]] = ...) -> None: ...

class GetAppTypeByIdRequest(_message.Message):
    __slots__ = ["app_type_id"]
    APP_TYPE_ID_FIELD_NUMBER: _ClassVar[int]
    app_type_id: int
    def __init__(self, app_type_id: _Optional[int] = ...) -> None: ...

class GetAppTypeByNameRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetApplicationByUidRequest(_message.Message):
    __slots__ = ["app_uid"]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    app_uid: str
    def __init__(self, app_uid: _Optional[str] = ...) -> None: ...

class GetCameraByUidRequest(_message.Message):
    __slots__ = ["camera_uid"]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    camera_uid: str
    def __init__(self, camera_uid: _Optional[str] = ...) -> None: ...

class ListApplicationByHostRequest(_message.Message):
    __slots__ = ["host"]
    HOST_FIELD_NUMBER: _ClassVar[int]
    host: str
    def __init__(self, host: _Optional[str] = ...) -> None: ...

class ListApplicationResponse(_message.Message):
    __slots__ = ["applications", "success"]
    APPLICATIONS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    applications: _containers.RepeatedCompositeFieldContainer[ApplicationFullData]
    success: bool
    def __init__(self, applications: _Optional[_Iterable[_Union[ApplicationFullData, _Mapping]]] = ..., success: bool = ...) -> None: ...

class ListMediaChannelsByCameraUidRequest(_message.Message):
    __slots__ = ["camera_uid"]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    camera_uid: str
    def __init__(self, camera_uid: _Optional[str] = ...) -> None: ...

class ListMediaChannelsResponse(_message.Message):
    __slots__ = ["media_channels", "success"]
    MEDIA_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    media_channels: _containers.RepeatedCompositeFieldContainer[MediaChannelsRequest]
    success: bool
    def __init__(self, media_channels: _Optional[_Iterable[_Union[MediaChannelsRequest, _Mapping]]] = ..., success: bool = ...) -> None: ...

class MediaChannelsRequest(_message.Message):
    __slots__ = ["app_uid", "camera_uid", "created_at", "is_enabled", "is_recording", "media_channel_id", "media_channel_info", "updated_at"]
    APP_UID_FIELD_NUMBER: _ClassVar[int]
    CAMERA_UID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_RECORDING_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CHANNEL_INFO_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    app_uid: str
    camera_uid: str
    created_at: _timestamp_pb2.Timestamp
    is_enabled: bool
    is_recording: bool
    media_channel_id: int
    media_channel_info: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, media_channel_id: _Optional[int] = ..., camera_uid: _Optional[str] = ..., app_uid: _Optional[str] = ..., media_channel_info: _Optional[str] = ..., is_enabled: bool = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_recording: bool = ...) -> None: ...

class MediaChannelsResponse(_message.Message):
    __slots__ = ["media_channels", "success"]
    MEDIA_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    media_channels: MediaChannelsRequest
    success: bool
    def __init__(self, media_channels: _Optional[_Union[MediaChannelsRequest, _Mapping]] = ..., success: bool = ...) -> None: ...
