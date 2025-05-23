import allure
from selene import browser as android_app, have

from stepik.mobile.custom_locator import by_id


class OnboardingPage:
    onboarding_pages_text = {
        "first_page": {
            "title": "Choose",
            "subtitle": "Browse through all the courses available on Stepik and choose what suits you",
        },
        "second_page": {
            "title": "Download",
            "subtitle": "Watch the video lectures online or download them for access without a connection",
        },
        "third_page": {
            "title": "Solve",
            "subtitle": "Complete the assignments using your mobile device",
        },
        "fourth_page": {
            "title": "Complete",
            "subtitle": "Set up reminders to study regularly and complete the courses faster",
        },
    }

    @allure.step("Проверка текста на странице онбординга")
    def check_onboarding_texts(self, title: str, subtitle: str):
        android_app.element(by_id("onboardingPageTitle")).should(have.text(title))
        android_app.element(by_id("onboardingPageSubtitle")).should(have.text(subtitle))
        return self

    @allure.step("Переход на следующую страницу онбординга")
    def go_to_next_onboarding_page(self):
        android_app.element(by_id("onboardingPageAction")).click()
        return self

    @allure.step("Пропуск онбординга")
    def skip_onboarding(self):
        android_app.element(by_id("closeOnboarding")).click()
        return self
