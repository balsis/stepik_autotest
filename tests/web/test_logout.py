import allure

from stepik.ui import web_app


@allure.parent_suite("Web")
@allure.suite("Выход из аккаунта на веб-сайте")
@allure.epic("Web")
@allure.feature("Выход из аккаунта на веб-сайте")
class TestLogout:

    @allure.sub_suite("Успешный выход")
    @allure.story("Выход из аккаунта")
    @allure.title("Успешный выход из аккаунта")
    def test_success_logout_from_account(self, authorized_user):
        web_app.navbar.open_profile_dropdown_menu()
        web_app.profile_menu.dropdown_menu_should_be_visible()
        web_app.profile_menu.logout_button()
        web_app.profile_menu.confirmation_popup_should_be_visible()
        web_app.profile_menu.confirm_logout()

        web_app.auth_widget.widget_should_be_visible()

    @allure.sub_suite("Отмена выхода из аккаунта")
    @allure.story("Отмена выхода из аккаунта")
    @allure.title("Отмена выхода из аккаунта")
    def test_cancel_logout_from_account(self, authorized_user):
        web_app.navbar.open_profile_dropdown_menu()
        web_app.profile_menu.dropdown_menu_should_be_visible()
        web_app.profile_menu.logout_button()
        web_app.profile_menu.confirmation_popup_should_be_visible()
        web_app.profile_menu.cancel_logout()

        web_app.navbar.learn_item_should_be_visible()
        web_app.navbar.last_activity_button_should_be_visible()
        web_app.navbar.profile_button_should_be_clickable()
        web_app.navbar.login_button_should_be_absent()
