from selene import browser, have, be


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
        android_management.element(("id", "org.stepic.droid:id/closeOnboarding")).click()
        android_management.element(("id", "org.stepic.droid:id/dismissButton")).should(be.clickable).click()
        android_management.element(("id", "org.stepic.droid:id/catalog")).should(be.selected)


onboarding_pages = {
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


def check_onboarding_texts(title: str, subtitle: str):
    browser.element(("id", "org.stepic.droid:id/onboardingPageTitle")).should(have.text(title))
    browser.element(("id", "org.stepic.droid:id/onboardingPageSubtitle")).should(have.text(subtitle))


def go_to_next_onboarding_page():
    browser.element(("id", "org.stepic.droid:id/onboardingPageAction")).click()


def test_onboarding_pages(android_management):
    check_onboarding_texts(
        title = onboarding_pages["first_page"]["title"],
        subtitle = onboarding_pages["first_page"]["subtitle"]
    )
    go_to_next_onboarding_page()

    check_onboarding_texts(
        title = onboarding_pages["second_page"]["title"],
        subtitle = onboarding_pages["second_page"]["subtitle"]
    )
    go_to_next_onboarding_page()

    check_onboarding_texts(
        title = onboarding_pages["third_page"]["title"],
        subtitle = onboarding_pages["third_page"]["subtitle"]
    )
    go_to_next_onboarding_page()

    check_onboarding_texts(
        title = onboarding_pages["fourth_page"]["title"],
        subtitle = onboarding_pages["fourth_page"]["subtitle"]
    )
    go_to_next_onboarding_page()
