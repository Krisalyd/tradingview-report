from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class StocksScreenerPage():
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver
    
    def check_visible_filters(self) -> tuple[list[str], WebElement]:     
        current_filters_list = []
        container_with_filters = self.driver.find_element(By.CSS_SELECTOR, ".pillsContainer-AUWRKzOl")
        filters = container_with_filters.find_elements(By.CSS_SELECTOR, ".wrapper-fkHAPqam")
        for filter in filters:
            current_filters_list.append(filter.text)
        return current_filters_list, container_with_filters
    
    def add_missing_filters(self, current_filters_list: list[str], container_filter: WebElement) -> None:
        try:
            sleep(3)
            control_class = container_filter.find_element(By.CSS_SELECTOR, ".controls-RMcYwJOr")
            add_filter_button = control_class.find_element(By.CSS_SELECTOR, "button[data-name=screener-add-new-filter]")

            # "Exchange" filter.
            if "Exchange" not in current_filters_list:
                add_filter_button.click()
                sleep(3)
                filter_field = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type filter name']")

                filter_field.click()
                sleep(3)
                filter_field.send_keys("Exchange")
                
        except Exception as exception_add_missing_filters:
            print(f"An error occurred while adding missing filters: \n{exception_add_missing_filters}")
            raise

    
    def apply_filters(self):
        filters = self.driver.find_elements(By.CSS_SELECTOR, ".wrapper-fkHAPqam")

        # Market
        for filter in filters:
            if filter.text.startswith("Market"):
                sleep(3)
                filter.click()

                main_countries = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for country in main_countries:
                    if country.text == "USA":
                        country.click()
                        break
            
                        