from selenium.webdriver import Chrome, ChromeOptions


def create_chrome_driver() -> Chrome:
    """Configure and create a Chrome WebDriver instance.

    Returns:
        Chrome: Instance of Chrome WebDriver.
    """         
    options_chrome = ChromeOptions()
    options_chrome.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36")
    options_chrome.add_argument("--disable-blink-features=AutomationControlled")
    options_chrome.add_experimental_option("excludeSwitches", ["enable-automation"])
    options_chrome.add_experimental_option("useAutomationExtension", False)
    options_chrome.page_load_strategy = "eager"
    driver = Chrome(options=options_chrome)
    return driver


