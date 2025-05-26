from selenium.webdriver import Chrome, ChromeOptions


def create_chrome_driver() -> Chrome:
    """Configure and create a Chrome WebDriver instance.

    Returns:
        Chrome: Instance of Chrome WebDriver.
    """         
    options_chrome = ChromeOptions()
    options_chrome.add_argument("--disable-blink-features=AutomationControlled")
    options_chrome.page_load_strategy = "eager"
    options_chrome.browser_version = "stable"
    driver = Chrome(options=options_chrome)
    return driver


