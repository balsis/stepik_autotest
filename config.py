from typing import Literal

from dotenv import load_dotenv
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from helpers.paths import file_path


load_dotenv()


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file = file_path(".env.base"))
    context: Literal['LOCAL', 'REMOTE'] = Field(default = 'REMOTE', description = "Execution context: local or CI")
    base_url: str = Field(default = 'https://stepik.org', description = "Base URL for API and Web testing")
    log_level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'] = Field(default = 'DEBUG', description = "Logs level")


class Credentials(BaseSettings):
    model_config = SettingsConfigDict(env_file = file_path(".env.credentials"))

    client_id: SecretStr
    client_secret: SecretStr
    selenoid_login: SecretStr
    selenoid_pass: SecretStr
    stepik_email: SecretStr
    stepik_password: SecretStr
    bstack_userName: SecretStr
    bstack_accessKey: SecretStr


class MobileConfig(BaseSettings):
    timeout: float = Field(default = 20.0, description = "Default timeout")
    app: str
    platformVersion: str = ''
    deviceName: str = ''
    udid: str = ''
    remote_url: str = ''


class WebConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file = file_path(".env.web"))
    web_timeout: float = Field(default = 15.0, description = "Default timeout")
    browser_name: str = 'chrome'
    browser_version: str = '127.0'
    window_size: str = ''
    selenoid_url: str = Field(default = "selenoid.autotests.cloud", description = "Default Selenoid URL")


class APIConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file = file_path(".env.api"))


class ProjectConfig(BaseSettings):
    base: BaseConfig = BaseConfig()
    web: WebConfig = WebConfig()
    credentials: Credentials = Credentials()


project_config = ProjectConfig()
