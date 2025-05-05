import allure
from selene import browser, have, be

from data.enums import CourseOptionsAsserts


class CatalogSearchPage:

    @property
    def all_course_cards(self):
        return browser.with_(timeout = 20).element('.course-cards').all('.course-cards__item')

    @property
    def prices(self):
        prices = browser.element('.course-cards').all('.format-price')
        prices.should(have.size_greater_than(0))
        return prices

    @property
    def certificates(self):
        certificates = browser.element('.course-cards').all('[data-type=certificate]')
        certificates.should(have.size_greater_than(0))
        return certificates

    @allure.step("Проверка, что все найденные курсы бесплатны")
    def all_courses_should_have_free_prices(self):
        self.prices.should(have.exact_text(CourseOptionsAsserts.FREE.value).each)

    @allure.step("Проверка, что все найденные курсы c сертификатом")
    def all_courses_should_have_certificate(self):
        self.certificates.should(have.exact_text(CourseOptionsAsserts.CERTIFICATE.value).each)

    @allure.step("Проверка наличия курса с наименованием {title} среди найденных")
    def should_have_course_with_title(self, title: str):
        self.all_course_cards.element_by_its('.course-card__title', have.exact_text(title)).should(be.visible)

    @allure.step("Проверка сообщения о неудачном поиске")
    def should_have_nothing_found_message(self, value):
        browser.element('.catalog__search-results-message').should(have.text(f'По запросу «{value}» ничего не найдено'))
        return self
