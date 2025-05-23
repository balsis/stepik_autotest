from config import project_config


class SelenoidData:
    SELENOID_LOGIN = project_config.credentials.selenoid_login.get_secret_value()
    SELENOID_PASS = project_config.credentials.selenoid_pass.get_secret_value()
    SELENOID_URL = project_config.web.selenoid_url


class UserData:
    STEPIK_EMAIL = project_config.credentials.stepik_email.get_secret_value()
    STEPIK_PASSWORD = project_config.credentials.stepik_password.get_secret_value()
    CLIENT_ID = project_config.credentials.client_id.get_secret_value()
    CLIENT_SECRET = project_config.credentials.client_secret.get_secret_value()


class BstackData:
    BSTACK_USERNAME = project_config.credentials.bstack_username.get_secret_value()
    BSTACK_ACCESS_KEY = project_config.credentials.bstack_accesskey.get_secret_value()
