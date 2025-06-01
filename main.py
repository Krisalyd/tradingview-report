from selenium.webdriver import Chrome
from drivers.chrome_driver import create_chrome_driver
from pages.login_page import LoginPage
from pages.stocks_screener_page import StocksScreenerPage
from config import get_env_str

BASE_URL: str = "https://www.tradingview.com/screener/"



def main():

    chrome_driver: Chrome | None = None

    try: 
        # Check if credentials are set
        email: str = get_env_str(key="LOGIN_EMAIL")
        password: str = get_env_str(key="LOGIN_PASSWORD")

        # Initialize the Chrome driver
        chrome_driver = create_chrome_driver()

        # Initialize the login page
        login_page = LoginPage(driver=chrome_driver, login_email=email, login_password=password)    
        login_page.sign_in(login_url=BASE_URL)

        stocks_screener_page = StocksScreenerPage(driver=chrome_driver)

        # Check current visible filters in screener page
        current_present_filters, container = stocks_screener_page.check_visible_filters()

        stocks_screener_page.apply_filters(current_filters=current_present_filters, container_with_filters=container)
    except:
        print("An error occurred during the execution of the script.")
    finally:
        if chrome_driver:
            chrome_driver.quit()

if __name__ == "__main__":
    main()
