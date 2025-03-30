import allure

from model import app

@allure.parent_suite("Вход и выход из аккаунта")
@allure.suite("Выход из аккаунта")
@allure.epic("Вход и выход из аккаунта")
@allure.feature("Выход из аккаунта")
class TestLogout:

    @allure.sub_suite("Успешный выход")
    @allure.story("Выход из аккаунта")
    @allure.title("Успешный выход из аккаунта")
    def test_success_logout_from_account(self, authorized_user):
        app.navbar.open_profile_dropdown_menu()
        app.profile_menu.dropdown_menu_should_be_visible()
        app.profile_menu.logout_button()
        app.profile_menu.confirmation_popup_should_be_visible()
        app.profile_menu.confirm_logout()

        app.auth_widget.widget_should_be_visible()

    @allure.sub_suite("Отмена выхода из аккаунта")
    @allure.story("Отмена выхода из аккаунта")
    @allure.title("Отмена выхода из аккаунта")
    def test_cancel_logout_from_account(self, authorized_user):
        app.navbar.open_profile_dropdown_menu()
        app.profile_menu.dropdown_menu_should_be_visible()
        app.profile_menu.logout_button()
        app.profile_menu.confirmation_popup_should_be_visible()
        app.profile_menu.cancel_logout()

        app.navbar.learn_item_should_be_visible()
        app.navbar.last_activity_button_should_be_visible()
        app.navbar.profile_button_should_be_clickable()
        app.navbar.login_button_should_be_absent()
