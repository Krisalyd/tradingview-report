from time import sleep
from random import uniform
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, WebDriverException
from utils.utilities import custom_delay

class LoginPage:
    def __init__(self, driver: WebDriver, login_email: str, login_password: str):
        self.driver = driver
        self.login_email = login_email
        self.login_password = login_password
    
    def sign_in(self, login_url: str) -> None:
        try:
            self.driver.get(login_url)

            # Find and click in the dropdown where the login button is located.
            custom_delay()
            find_login_dropdown_button = self.driver.find_element(By.CSS_SELECTOR, ".tv-header__user-menu-button.tv-header__user-menu-button--anonymous.js-header-user-menu-button")
            find_login_dropdown_button.click()
            self.driver.implicitly_wait(5)

            # Open sign in page.
            custom_delay()         
            sign_in_button = self.driver.find_element(By.CSS_SELECTOR,"button[data-name=header-user-menu-sign-in]")
            sign_in_button.click()

            # Click on the "Sign in with email" button.
            custom_delay()
            login_with_email_button = self.driver.find_element(By.CSS_SELECTOR, "button[name='Email']")
            login_with_email_button.click()
            
            # Enter email and password.
            custom_delay()
            email_input = self.driver.find_element(By.CSS_SELECTOR, "#id_username")
            email_input.send_keys(self.login_email)
            custom_delay()
            password_input = self.driver.find_element(By.CSS_SELECTOR, "#id_password")
            password_input.send_keys(self.login_password)
            
            # TODO: Testar manipulação de IP para evitar bloqueios.
            # Sign in button click
            sign_in_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-overflow-tooltip-text='Sign in']")
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
            
