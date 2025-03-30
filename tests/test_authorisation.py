import allure

from data.data import UserData
from data import fake
from model import app


@allure.parent_suite("Вход и выход из аккаунта")
@allure.suite("Авторизация")
@allure.epic("Вход и выход из аккаунта")
@allure.feature("Авторизация")
class TestAuthorisation:

    @allure.sub_suite("Авторизация с валидными данными")
    @allure.story("Авторизация с валидными данными")
    @allure.title("Авторизация с валидным email и паролем")
    def test_login_with_valid_email_password(self):
        app.catalog_page.open()
        app.navbar.open_sign_in_form()
        app.auth_widget.widget_should_be_visible()
        app.auth_widget.fill_email_password_values(email = UserData.STEPIK_EMAIL, password = UserData.STEPIK_PASSWORD)
        app.auth_widget.submit_button()

        app.navbar.learn_item_should_be_visible()
        app.navbar.last_activity_button_should_be_visible()
        app.navbar.profile_button_should_be_clickable()
        app.navbar.login_button_should_be_absent()

    @allure.sub_suite("Авторизация с невалидными данными")
    @allure.story("Авторизация с невалидными данными")
    @allure.title("Авторизация с невалидными email и паролем")
    def test_login_with_invalid_email_password(self):
        app.catalog_page.open()
        app.navbar.open_sign_in_form()
        app.auth_widget.widget_should_be_visible()
        app.auth_widget.fill_email_password_values(email = fake.wrong_email, password = fake.wrong_password)
        app.auth_widget.submit_button()

        app.auth_widget.alert_should_be_visible()


