import allure

from data import fake
from data.data import UserData
from stepik.ui import web_app


@allure.parent_suite("Web")
@allure.suite("Авторизация")
@allure.epic("Web")
@allure.feature("Авторизация")
class TestAuthorisation:

    @allure.sub_suite("Авторизация с валидными данными")
    @allure.story("Авторизация с валидными данными")
    @allure.title("Авторизация с валидным email и паролем")
    def test_login_with_valid_email_password(self):
        web_app.catalog_page.open()
        web_app.navbar.open_sign_in_form()
        web_app.auth_widget.widget_should_be_visible()
        web_app.auth_widget.fill_email_password_values(email = UserData.STEPIK_EMAIL, password = UserData.STEPIK_PASSWORD)
        web_app.auth_widget.submit_button()

        web_app.navbar.learn_item_should_be_visible()
        web_app.navbar.last_activity_button_should_be_visible()
        web_app.navbar.profile_button_should_be_clickable()
        web_app.navbar.login_button_should_be_absent()

    @allure.sub_suite("Авторизация с невалидными данными")
    @allure.story("Авторизация с невалидными данными")
    @allure.title("Авторизация с невалидными email и паролем")
    def test_login_with_invalid_email_password(self):
        web_app.catalog_page.open()
        web_app.navbar.open_sign_in_form()
        web_app.auth_widget.widget_should_be_visible()
        web_app.auth_widget.fill_email_password_values(email = fake.wrong_email, password = fake.wrong_password)
        web_app.auth_widget.submit_button()

        web_app.auth_widget.alert_should_be_visible()
