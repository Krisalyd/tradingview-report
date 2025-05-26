from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from utils.utilities import custom_delay

class StocksScreenerPage():
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver
    
    def check_if_filters_are_visible(self):
        visible_filters = self.driver.find_elements(By.CSS_SELECTOR, ".pillsContainer-AUWRKzOl")
        for filter in visible_filters:
            print(filter.text)
    
    def apply_standard_filters(self):
        # Filter country
        country_filter = self.driver.find_element(By.CSS_SELECTOR, "div[class='pill-fkHAPqam small-fkHAPqam secondary-fkHAPqam small-fkHAPqam valueNotSelected-fkHAPqam'] div[class='content-Ms2EU9Vx']")
        country_filter.click()      
        usa_market = self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(13) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
        usa_market.click()