from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class StocksScreenerPage():
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver
    
    # TODO: Implementar método para verificar filtros visiveis e buscar os faltantes
    def check_visible_filters(self):
        self.driver.find_element(By.CSS_SELECTOR,)
    
    def apply_filters(self):
        filters = self.driver.find_elements(By.CSS_SELECTOR, ".wrapper-fkHAPqam")

        # Market
        for filter in filters:
            if filter.text.startswith("Market"):
                sleep(2)
                filter.click()

                main_countries = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for country in main_countries:
                    if country.text == "USA":
                        country.click()
                        break
            
                        