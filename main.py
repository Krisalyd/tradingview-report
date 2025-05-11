from config import BASE_URL, LOGIN_EMAIL, LOGIN_PASSWORD
from drivers.chrome_driver import ChromeDriver
from selenium.webdriver import Chrome
from pages.login_page import LoginPage


def main():
    chrome_driver: Chrome = ChromeDriver.create_chrome_driver()
    
    try:
        login_page = LoginPage(driver=chrome_driver)
        login_page.sign_in(login_url=BASE_URL)
    except:
        pass
    finally:
        chrome_driver.quit()

main()


"""
driver = webdriver.Chrome()
driver.get("https://selenium.dev/")
driver.quit()"""
"""
driver = webdriver.Chrome()

driver.get("https://selenium.dev/documentation")
assert "Selenium" in driver.title

elem = driver.find_element(by=By.ID, value="m-documentationwebdriver")
elem.click()
assert "WebDriver" in driver.title

driver.quit()
"""