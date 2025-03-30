import allure
from selene import browser, be, have


class AuthWidget:

    @allure.step("Проверка, что виджет авторизации отображается")
    def widget_should_be_visible(self):
        browser.element('.auth-widget').should(be.visible)
        return self

    @allure.step("Заполнение полей email и пароля")
    def fill_email_password_values(self, email: str, password: str):
        browser.element('#id_login_email').type(email)
        browser.element('#id_login_password').type(password)
        return self

    @allure.step("Нажатие на кнопку отправки формы авторизации")
    def submit_button(self):
        browser.element('[type="submit"]').click()
        return self

    @allure.step("Проверка, что ошибка авторизации отображается")
    def alert_should_be_visible(self):
        browser.element('[role="alert"]').should(have.text('E-mail адрес и/или пароль не верны.'))
        return self
