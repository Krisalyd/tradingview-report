from time import sleep
from random import uniform

def custom_delay() -> None:
    """Pause the execution for a random duration between 3 to 8 seconds."""
    sleep(uniform(3, 8))

def custom_filters() -> dict[str, str | list[str | int | float]]:
    """ Create a dictionary of custom filters for the stocks screener.

    Returns:
        dict: A dictionary containing custom filters for the stocks screener.
    """    
    filters_dict = {
        "Market": "USA",
        "ROE": ["Trailing 12 Months", "Above", "Value", 9],
        "Market Cap": "300 M",
        "Exchange": ["NASDAQ", "NYSE"],
        "Net debt / EBITDA": ["Trailing 12 Months", "Below", "Value", 3],
        "ROA": ["Trailing 12 Months", "Above", "Value", 9],
        "Div yield": ["Trailing 12 Months", "Above", "Value", 1.8]
    }
    return filters_dict
    