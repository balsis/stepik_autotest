import allure
from selene import browser, be

from stepik.ui.utils import page_is_loaded


class LearnPage:

    @allure.step('Открытие страницы "Мое обучение"')
    def open(self):
        browser.open('/learn')
        browser.wait.until(page_is_loaded)

    @allure.step('Навигационное меню раздела "Моё обучение" отображается')
    def learn_navigation_menu_should_be_visible(self):
        browser.element('.learn-nav__menu').should(be.visible)
        return self

    @allure.step('Открыть список курсов "Прохожу"')
    def open_active_courses(self):
        browser.element('.data-item=courses-active').click()
        return self

    @allure.step('Открыть список курсов "Хочу пройти"')
    def open_courses_wishlist(self):
        browser.element('.data-item=courses-wishlist').click()
        return self

    @allure.step('Открыть список курсов "Избранные"')
    def open_favorite_courses(self):
        browser.element('[data-item=courses-favorites]').click()
        return self
