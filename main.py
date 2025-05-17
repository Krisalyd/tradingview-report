from selenium.webdriver import Chrome
from config import LOGIN_EMAIL, LOGIN_PASSWORD
from drivers.chrome_driver import create_chrome_driver
from pages.login_page import LoginPage

BASE_URL = "https://www.tradingview.com/screener/"

chrome_driver: Chrome = create_chrome_driver()

def main():
    
    try: 
        login_page = LoginPage(driver=chrome_driver)
        login_page.sign_in(login_url=BASE_URL)
    except:
        print("An error occurred during the execution of the script.")
    finally:
        chrome_driver.quit

if __name__ == "__main__":
    main()
