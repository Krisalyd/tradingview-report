from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, WebDriverException 


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def sign_in(self, login_url: str):
        try:
            self.driver.get(login_url)

            # Find and click in the dropdown where the login button is located.
            find_login_dropdown_button = self.driver.find_element(By.CSS_SELECTOR, ".tv-header__user-menu-button.tv-header__user-menu-button--anonymous.js-header-user-menu-button")
            find_login_dropdown_button.click()

            # Open sign in page.
            sign_in_button = self.driver.find_element(By.CSS_SELECTOR,"button[data-name=header-user-menu-sign-in]")
            sign_in_button.click()

            

        except NoSuchElementException as e:
            print(f"Element not found during sign in process: \n{e}")
        except TimeoutException as e:
            print(f"Timeout occurred during sign in process: \n{e}")
        except ElementNotInteractableException as e:
            print(f"Element not interactable during sign in process: \n{e}")
        except WebDriverException as e:
            print(f"WebDriver exception occurred during sign in process: \n{e}")
        except Exception as e:
            print(f"An unexpected error occurred during sign in process: \n{e}")
            
