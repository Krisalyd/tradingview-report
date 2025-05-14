from selenium.webdriver import Chrome
from config import LOGIN_EMAIL, LOGIN_PASSWORD
from drivers.chrome_driver import ChromeDriver
from pages.login_page import LoginPage

BASE_URL = "https://www.tradingview.com/screener/"

def main():
    try:
        chrome_driver: Chrome = ChromeDriver.create_chrome_driver()
        login_page = LoginPage(driver=chrome_driver)
        login_page.sign_in(login_url=BASE_URL)
    except:
        pass
    finally:
        chrome_driver.quit()

if __name__ == "__main__":
    main()
