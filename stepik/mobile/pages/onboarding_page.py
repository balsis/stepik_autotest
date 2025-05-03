from selene import browser as android_app


class OnboardingPage:

    def skip_onboarding(self):
        android_app.element(("id", "org.stepic.droid:id/closeOnboarding")).click()
        return self

    def go_to_next_onboarding_page(self):
        android_app.element()
        return self
