import allure

from data import fake
from stepik.ui import web_app


@allure.parent_suite("Web")
@allure.suite("Поиск на веб-сайте")
class TestNavbarSearch:

    @allure.sub_suite("Поиск из навигационной панели")
    @allure.title("Поиск курса с валидным названием из навигационной панели")
    def test_search_course_with_valid_keyword_from_navbar(self):
        web_app.catalog_page.open()
        web_app.navbar.find_course(course_name = "Инди-курс программирования на Python")
        web_app.catalog_search_page.should_have_course_with_title(title = "Инди-курс программирования на Python")

    @allure.sub_suite("Поиск из навигационной панели")
    @allure.title("Поиск курса с невалидным названием из навигационной панели")
    def test_search_course_with_invalid_keyword_from_navbar(self):
        web_app.catalog_page.open()
        web_app.navbar.find_course(course_name = fake.random_invalid_search_keyword)
        web_app.catalog_search_page.should_have_nothing_found_message(value = fake.random_invalid_search_keyword)


@allure.parent_suite("Web")
@allure.suite("Поиск на веб-сайте")
@allure.epic("Web")
@allure.feature("Поиск на веб-сайте")
class TestCatalogSearch:

    @allure.sub_suite("Поиск курса в Каталоге")
    @allure.title("Поиск курса с валидным названием в Каталоге")
    def test_search_course_with_valid_keyword_from_catalog(self):
        web_app.catalog_page.open()
        web_app.catalog_page.fill_course_name(course_name = "Инди-курс программирования на Python")
        web_app.catalog_page.submit_search_button()
        web_app.catalog_search_page.should_have_course_with_title(title = "Инди-курс программирования на Python")

    @allure.sub_suite("Поиск курса в Каталоге")
    @allure.title("Поиск в Каталоге бесплатных курсов")
    def test_search_free_courses(self):
        web_app.catalog_page.open()
        web_app.catalog_page.click_free_checkbox()
        web_app.catalog_page.submit_search_button()
        web_app.catalog_search_page.all_courses_should_have_free_prices()

    @allure.sub_suite("Поиск курса в Каталоге")
    @allure.title("Поиск в Каталоге курсов с сертификатами")
    def test_search_courses_with_certs(self):
        web_app.catalog_page.open()
        web_app.catalog_page.click_certificate_checkbox()
        web_app.catalog_page.submit_search_button()
        web_app.catalog_search_page.all_courses_should_have_certificate()

    @allure.sub_suite("Поиск курса в Каталоге")
    @allure.title("Поиск курса с невалидным названием в Каталоге")
    def test_search_course_with_invalid_keyword_from_catalog(self):
        web_app.catalog_page.open()
        web_app.catalog_page.fill_course_name(course_name = fake.random_invalid_search_keyword)
        web_app.catalog_page.submit_search_button()
        web_app.catalog_search_page.should_have_nothing_found_message(value = fake.random_invalid_search_keyword)
