import allure
from selene import browser, be


class ProfileDropdownMenu:

    @allure.step("Проверка, что выпадающее меню профиля отображается")
    def dropdown_menu_should_be_visible(self):
        browser.element('.drop-down__body').should(be.visible)
        return self

    @allure.step("Открытие страницы профиля через меню профиля")
    def open_profile(self):
        browser.element('[data-qa=menu-item-profile]').should(be.clickable).click()
        return self

    @allure.step("Открытие настроек профиля через меню профиля")
    def open_settings(self):
        browser.element('[data-qa=menu-item-settings]').should(be.clickable).click()
        return self

    @allure.step("Нажатие на кнопку выхода через меню профиля")
    def logout_button(self):
        browser.element('[data-qa=menu-item-logout]').should(be.clickable).click()
        return self

    @allure.step("Проверка, что подтверждающее окно выхода отображается")
    def confirmation_popup_should_be_visible(self):
        browser.element('.modal-popup__container').should(be.visible)
        return self

    @allure.step("Подтверждение выхода")
    def confirm_logout(self):
        browser.element('//button[text()="OK"]').should(be.clickable).click()
        return self

    @allure.step("Отмена выхода")
    def cancel_logout(self):
        browser.element('//button[text()="Отмена"]').should(be.clickable).click()
        return self
