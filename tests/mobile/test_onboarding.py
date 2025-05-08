from selene import have

from stepik.mobile import android_app


class TestOnboarding:
    def test_onboarding_page(self, android_management):
        # First onboarding page
        android_management.element(("id", "org.stepic.droid:id/onboardingPageTitle")).should(have.text("Choose"))
        android_management.element(("id", "org.stepic.droid:id/onboardingPageSubtitle")).should(
            have.text("Browse through all the courses available on Stepik and choose what suits you"))
        android_management.element(("id", "org.stepic.droid:id/onboardingPageAction")).click()
        # Second onboarding page
        android_management.element(("id", "org.stepic.droid:id/onboardingPageTitle")).should(have.text("Download"))
        android_management.element(("id", "org.stepic.droid:id/onboardingPageSubtitle")).should(
            have.text("Watch the video lectures online or download them for access without a connection"))
        android_management.element(("id", "org.stepic.droid:id/onboardingPageAction")).click()
        # Third onboarding page
        android_management.element(("id", "org.stepic.droid:id/onboardingPageTitle")).should(have.text("Solve"))
        android_management.element(("id", "org.stepic.droid:id/onboardingPageSubtitle")).should(
            have.text("Complete the assignments using your mobile device"))
        android_management.element(("id", "org.stepic.droid:id/onboardingPageAction")).click()
        # Last onboarding page
        android_management.element(("id", "org.stepic.droid:id/onboardingPageTitle")).should(have.text("Complete"))
        android_management.element(("id", "org.stepic.droid:id/onboardingPageSubtitle")).should(
            have.text("Set up reminders to study regularly and complete the courses faster"))
        android_management.element(("id", "org.stepic.droid:id/onboardingPageAction")).click()

    def test_skip_onboarding(self, android_management):
        android_app.onboarding_page.skip_onboarding()



def test_onboarding_pages(android_management):
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
