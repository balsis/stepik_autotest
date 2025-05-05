import allure
import pytest
from selene import browser
from selenium import webdriver

from data.data import SelenoidData, UserData
from helpers.web import ui_attach


def pytest_addoption(parser):
    parser.addoption('--browser_version', help = 'Выберите версию браузера', default = '127.0')
    parser.addoption('--executor', help = 'Выберите executor: local или selenoid', default = 'selenoid')


@allure.step("Запуск браузера")
@pytest.fixture(scope = 'function', autouse = True)
def remote_browser(request):
    executor = request.config.getoption('--executor')
    browser_version = request.config.getoption('--browser_version')

    options = webdriver.ChromeOptions()
    options.page_load_strategy = "eager"
    options.add_argument('--incognito')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36')
    browser.config.driver_options = options
    browser.config.base_url = 'https://stepik.org'
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.config.timeout = 10
    if executor == 'selenoid':
        with allure.step(f"Инициализация удалённого браузера Chrome {browser_version} через Selenoid"):
            selenoid_capabilities = {
                "browserName": "chrome",
                "browserVersion": browser_version,
                "selenoid:options": {
                    "enableVNC": True,
                    "enableVideo": True
                }
            }
            options.capabilities.update(selenoid_capabilities)
            browser.config.driver = webdriver.Remote(
                command_executor = f"https://{SelenoidData.SELENOID_LOGIN}:{SelenoidData.SELENOID_PASS}@{SelenoidData.SELENOID_URL}/wd/hub",
                options = options
            )
    else:
        with allure.step(f"Инициализация локального браузера Chrome"):
            browser.config.driver = webdriver.Chrome(options = options)

    yield browser

    ui_attach.add_screenshot(browser)
    ui_attach.add_html(browser)
    ui_attach.add_logs(browser)
    if executor == 'selenoid':
        ui_attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope = "function")
def authorized_user(remote_browser):
    from helpers.web.api_client import AuthHelper
    cookies = AuthHelper().login(email = UserData.STEPIK_EMAIL, password = UserData.STEPIK_PASSWORD)
    csrftoken, sessionid = cookies.get('csrftoken'), cookies.get('sessionid')
    browser.open('/').with_(timeout = 20)
    try:
        browser.driver.add_cookie({"name": "csrftoken", "value": csrftoken})
        browser.driver.add_cookie({"name": "sessionid", "value": sessionid})
    except Exception as e:
        print(f"Не удалось установить cookie - {e}")
    browser.driver.refresh()
    yield browser
