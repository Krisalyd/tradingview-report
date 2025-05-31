from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from utils.utilities import custom_delay

class StocksScreenerPage():
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver
    
    def check_visible_filters(self) -> list[str]:       
        """ Check visible filters in the stocks screener page.

        Returns:
            list[str]: A list of visible filters in the stocks screener page.
        """
        visible_filters_container = self.driver.find_elements(By.CSS_SELECTOR, ".pillsContainer-AUWRKzOl")
        filter_names: list[str] = visible_filters_container[0].text.split("\n")
        return filter_names
    
    def apply_filters(self):
        # Find the filters container
        filters_container = self.driver.find_element(By.CSS_SELECTOR, ".pillsContainer-AUWRKzOl")

        # Iterate through each filter
        filters = filters_container.find_elements(By.CSS_SELECTOR, "button[data-name='screener-add-new-filter']")
        for filter in filters:
            print(f"Filtro atual: {filter.text}")
        
        