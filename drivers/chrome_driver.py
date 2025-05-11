from selenium.webdriver import Chrome, ChromeOptions


class ChromeDriver:
    def create_chrome_driver() -> Chrome:
        """Configure and create a Chrome WebDriver instance.

        Returns:
            webdriver.Chrome: Instance of Chrome WebDriver.
        """         
        options_chrome = ChromeOptions()
        options_chrome.page_load_strategy = "eager"
        options_chrome.accept_insecure_certs = True
        options_chrome.browser_version = "stable"
        driver = Chrome(options=options_chrome)
        return driver


