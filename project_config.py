from pydantic import BaseSettings, Field


class BaseConfig(BaseSettings):
    context: str = Field(default = 'local', description = "Testing context: local, dev, prod, etc.")
    timeout: float = Field(default = 10.0, description = "Default timeout for actions")
    base_url: str = Field(default = '', description = "Base URL for API and Web testing")


class MobileConfig(BaseSettings):
    bstack_userName: str = ''
    bstack_accessKey: str = ''
    app: str
    platformVersion: str = ''
    deviceName: str = ''
    udid: str = ''
    remote_url: str = ''


class APIConfig(BaseSettings):
    api_base_path: str = '/api/v1'
    api_token: str = ''


class UIConfig(BaseSettings):
    browser_name: str = 'chrome'
    browser_version: str = ''
    window_size: str = '1920x1080'
    remote_driver_url: str = ''


class ProjectConfig(BaseSettings):
    base: BaseConfig = BaseConfig()
    mobile: MobileConfig = MobileConfig()
    api: APIConfig = APIConfig()
    ui: UIConfig = UIConfig()
