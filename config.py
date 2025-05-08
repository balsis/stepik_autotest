import os
from typing import Literal

from appium.options.android import UiAutomator2Options
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
    model_config = SettingsConfigDict(
        env_file = file_path(f".env.mobile.{os.getenv('context', 'local')}")
    )
    mobile_timeout: float = Field(default = 20.0, description = "Default timeout")
    app: str
    platformName: str = ''
    platformVersion: str = ''
    deviceName: str = ''
    remote_url: str = ''

    def get_options(self):
        capabilities = {
            'platformVersion': self.platformVersion,
            'deviceName': self.deviceName,
            'app': project_config.mobile.app if project_config.mobile.app.startswith('bs://') else file_path(self.app),
            'appWaitActivity': "org.wikipedia.*"
        }

        if self.context == 'bstack':
            capabilities['bstack:options'] = {
                'projectName': 'Mobile project',
                'buildName': 'browserstack-build-1',
                'sessionName': f'{self.platformName} test',
                'userName': self.bstack_userName,
                'accessKey': self.bstack_accessKey,
            }

        if self.platformName == 'android':
            return UiAutomator2Options().load_capabilities(capabilities)


class WebConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file = file_path(".env.web"))
    web_timeout: float = Field(default = 15.0, description = "Default timeout")
    browser_name: str = 'chrome'
    browser_version: str = '127.0'
    window_size: str = ''
    selenoid_url: str = Field(default = "selenoid.autotests.cloud", description = "Default Selenoid URL")


class ProjectConfig(BaseSettings):
    base: BaseConfig = BaseConfig()
    credentials: Credentials = Credentials()
    web: WebConfig = WebConfig()
    mobile: MobileConfig = MobileConfig()


project_config = ProjectConfig()