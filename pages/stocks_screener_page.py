from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from utils.utilities import custom_delay

class StocksScreenerPage():
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver
    
    def check_visible_filters(self) -> tuple[list[str], list[WebElement]]:       
        """Check visible filters in the stocks screener page.

        Returns:
            tuple[list[str], list[WebElement]]: Returns a tuple containing a list of filter names and a list of WebElements representing the visible filters.
        """        
        visible_filters_container = self.driver.find_elements(By.CSS_SELECTOR, ".pillsContainer-AUWRKzOl")
        filter_names = visible_filters_container[0].text.split("\n")
        return filter_names, visible_filters_container
    
    def apply_filters(self, current_filters: list[str], container_with_filters: list[WebElement]):
        # Configure each filter individually
        # Market
        # TODO: Debugar para entender do que o container_with_filters é composto
        for filter in container_with_filters:
            print(f"Cheguei no filtro: {filter.text}")
            
        