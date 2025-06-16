from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

class StocksScreenerPage():
    def __init__(self, driver: Chrome) -> None:
        self.driver = driver

    def define_table_columns(self) -> list[str]:
        """ Define the columns to be used in the stocks screener table.

        Returns:
            list[str]: A list of column names to be used in the stocks screener table.
        """        
        columns: list[str]

        data_field_columns = [
            "Price",
            "MarketCap",
            "PriceToEarnings",
            "DividendsYield|ttm",
            "Sector",
            "Exchange",
            "NetDebtToEbitda|ttm",
            "Industry",
            "PriceToBook"
            "ReturnOnEquity|ttm",
            "ReturnOnAssets|ttm"
            "ReturnOnInvestedCapital|ttm",
        ]
        return data_field_columns

    def select_columns(self) -> None:
        current_columns: list[WebElement] = []
        column_data_field: list[str] = []
        add_column_button: WebElement = self.driver.find_element(By.CSS_SELECTOR, "button[data-name='screener-add-column']")

        try:
            current_columns = self.driver.find_elements(By.TAG_NAME, "th")
            for column in current_columns:
                column_data_field.append(column.get_dom_attribute("data-field"))

            # Add the columns that are not currently selected
            # Exchange
            if "Exchange" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Exchange")

        except Exception as exception_select_columns:
            print("An error occurred while selecting columns in the stocks screener page.")
            raise exception_select_columns
    

    

            
                        