import allure
from selene import browser, have, be


class Navbar:

    @allure.step("Проверка, что логотип в панели навигации кликабелен")
    def logo_link_should_be_clickable(self):
        browser.element('navbar__logo-link').should(be.clickable)
        return self

    @allure.step("Открытие формы авторизации через панель навигации")
    def open_sign_in_form(self):
        browser.element('.navbar__auth_login').click()
        return self

    @allure.step("Поиск курса: {course_name} через панель навигации")
    def find_course(self, course_name):
        browser.element(".navbar__search-input").click()
        browser.element(".navbar__search-input").type(course_name).press_enter()
        return self

    @allure.step("Проверка, что в панели навигации отображается элемент 'Моё обучение'")
    def learn_item_should_be_visible(self):
        browser.element('[data-navbar-item="learn"]').should(be.visible).should(have.text('Моё обучение'))
        return self

    @allure.step("Проверка, что кнопка последней активности в панели навигации кликабельна")
    def last_activity_button_should_be_visible(self):
        browser.element('.learn-last-activity-dropdown').should(be.clickable)
        return self

    @allure.step("Проверка, что кнопка профиля кликабельна")
    def profile_button_should_be_clickable(self):
        browser.element('.navbar__profile-toggler').should(be.clickable)
        return self

    @allure.step("Проверка, что кнопка входа в панели навигации отсутствует")
    def login_button_should_be_absent(self):
        browser.element('.navbar__auth_login').should(be.not_.in_dom)
        return self

    @allure.step("Открытие выпадающего меню профиля")
    def open_profile_dropdown_menu(self):
        browser.element('.navbar__profile-toggler').click()
        return self
