import allure
import pytest
from appium import webdriver
from selene import browser

from config import project_config
from helpers.mobile import mobile_attach


@pytest.fixture(scope = "function")
def android_management():
    options = project_config.mobile.get_options()
    with allure.step('Инициализация тестовой сессии'):
        browser.config.driver = webdriver.Remote(
            project_config.mobile.remote_url,
            options = options
        )
    browser.config.timeout = project_config.mobile.mobile_timeout
    yield browser
    mobile_attach.add_screenshot()
    mobile_attach.add_page_source_xml()
    session_id = browser.driver.session_id
    with allure.step('Завершение тестовой сессии'):
        browser.quit()
    if project_config.base.context == 'remote':
        mobile_attach.add_bstack_video(session_id)
