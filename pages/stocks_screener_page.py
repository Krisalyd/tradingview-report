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
            # Price
            if "Price" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Price")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Exchange":
                        item.click()
                        break

            # MarketCap
            if "MarketCap" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Market capitalization")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Market capitalization":
                        item.click()
                        break

            # Exchange
            if "Exchange" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Exchange")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Exchange":
                        item.click()
                        break
            
            # PriceToEarnings
            if "PriceToEarnings" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Price to earnings ratio")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Price to earnings ratio":
                        item.click()
                        break

            # DividendsYield|ttm
            if "DividendsYield|ttm" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Dividend yield %")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Dividend yield %":
                        item.click()
                        sleep(1.5)
                        self.driver.find_element(By.CSS_SELECTOR, "button[data-overflow-tooltip-text='Add column']").click()
                        break

            # Sector
            if "Sector" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Sector")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Sector":
                        item.click()
                        break

            # NetDebtToEbitda|ttm
            if "NetDebtToEbitda|ttm" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Net debt to EBITDA")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Net debt to EBITDA":
                        item.click()
                        sleep(1)
                        self.driver.find_element(By.CSS_SELECTOR, "button[data-overflow-tooltip-text='Add column']").click()
                        break

            # Industry
            if "Industry" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Industry")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Industry":
                        item.click()
                        break
            
            # PriceToBook
            if "PriceToBook" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Price to book ratio")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Price to book ratio":
                        item.click()
                        break
            
            # ReturnOnEquity|ttm
            if "ReturnOnEquity|ttm" not in column_data_field:
                add_column_button.click()
                sleep(1.5)
                self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type column name']").send_keys("Return on equity %")
                columns_options = self.driver.find_elements(By.CSS_SELECTOR, ".button-Lsy3A2H8")
                for item in columns_options:
                    if item.text == "Return on equity %":
                        item.click()
                        sleep(1)
                        self.driver.find_element(By.CSS_SELECTOR, "button[data-overflow-tooltip-text='Add column']").click()
                        break
                

        except Exception as exception_select_columns:
            print(f"An error occurred while selecting columns in the stocks screener page: \n{exception_select_columns}")
            raise
    

    

            
                        