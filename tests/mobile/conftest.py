import pytest
from appium import webdriver
from appium.options.common import AppiumOptions
from selene import browser

from helpers.common import file_path


@pytest.fixture(scope = "function")
def android_management():
    caps = {
        "platformName": "Android",
        "automationName": "UIAutomator2",
        "deviceName": "emulator-5554",
        "app": file_path("stepik.apk"),
        "autoGrantPermissions": True
    }
    options = AppiumOptions().load_capabilities(caps)
    browser.config.driver = webdriver.Remote("http://127.0.0.1:4723", options = options)
    browser.config.timeout = 12
    yield browser
    browser.quit()
