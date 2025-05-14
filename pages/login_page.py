from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils.helpers import custom_exception_traceback

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def sign_in(self, login_url: str):
        try:
            self.driver.get(login_url)
        except NoSuchElementException as e:
            #TODO: Criar exceção após finalizar de criar uma função em helpers.py que configura o traceback.
            print(f"Element not found during sign in process: \n{custom_exception_traceback(e)}")
        except TimeoutException as e:
            print(f"Timeout occurred during sign in process: \n{custom_exception_traceback(e)}")
            
