from selenium.webdriver import Chrome
from drivers.chrome_driver import create_chrome_driver
from pages.login_page import LoginPage
from pages.stocks_screener_page import StocksScreenerPage
from config import get_env_str

BASE_URL: str = "https://www.tradingview.com/screener/"



def main():
    required_columns: list[str]
    chrome_driver: Chrome | None = None
    columns: list[str] = []

    try: 
        # Check if credentials are set
        email: str = get_env_str(key="LOGIN_EMAIL")
        password: str = get_env_str(key="LOGIN_PASSWORD")

        # Initialize the Chrome driver
        chrome_driver = create_chrome_driver()

        # Initialize the login page
        login_page = LoginPage(driver=chrome_driver, login_email=email, login_password=password)    
        login_page.sign_in(login_url=BASE_URL)

        # Initialize the stocks screener page
        stocks_screener_page = StocksScreenerPage(driver=chrome_driver)

        # Setup table column
        stocks_screener_page.select_columns()

        # Required columns for the report
        columns = stocks_screener_page.define_table_columns()

        # Get column position
        dict_columns = stocks_screener_page.get_column_position(columns_list=columns)

        # TODO: Implement method to collect data based on the columns positions
        # Collect data
        #stocks_screener_page.collect_stocks_data(required_columns=columns)

    except Exception as exception_main:
        print("An error occurred during the execution of the script.")
    finally:
        if chrome_driver:
            chrome_driver.quit()

if __name__ == "__main__":
    main()
