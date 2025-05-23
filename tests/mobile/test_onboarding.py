import allure

from stepik.mobile import android_app


@allure.parent_suite("Mobile")
@allure.suite("Онбординг на мобильном устройстве")
class TestOnboarding:

    @allure.sub_suite("Онбординг")
    @allure.title("Пропуск онбординга")
    def test_skip_onboarding(self, android_management):
        android_app.onboarding_page.skip_onboarding()
        android_app.sign_in_page.check_sign_in_page_is_opened()

    @allure.sub_suite("Онбординг")
    @allure.title("Проверка страниц онбординга")
    def test_onboarding_pages(self, android_management):
        android_app.onboarding_page.check_onboarding_texts(
            title = android_app.onboarding_page.onboarding_pages_text["first_page"]["title"],
            subtitle = android_app.onboarding_page.onboarding_pages_text["first_page"]["subtitle"]
        )
        android_app.onboarding_page.go_to_next_onboarding_page()

        android_app.onboarding_page.check_onboarding_texts(
            title = android_app.onboarding_page.onboarding_pages_text["second_page"]["title"],
            subtitle = android_app.onboarding_page.onboarding_pages_text["second_page"]["subtitle"]
        )
        android_app.onboarding_page.go_to_next_onboarding_page()

        android_app.onboarding_page.check_onboarding_texts(
            title = android_app.onboarding_page.onboarding_pages_text["third_page"]["title"],
            subtitle = android_app.onboarding_page.onboarding_pages_text["third_page"]["subtitle"]
        )
        android_app.onboarding_page.go_to_next_onboarding_page()

        android_app.onboarding_page.check_onboarding_texts(
            title = android_app.onboarding_page.onboarding_pages_text["fourth_page"]["title"],
            subtitle = android_app.onboarding_page.onboarding_pages_text["fourth_page"]["subtitle"]
        )
        android_app.onboarding_page.go_to_next_onboarding_page()
