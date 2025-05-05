from selene import browser


def page_is_loaded():
    return browser.driver.execute_script("return document.readyState") == "complete"


