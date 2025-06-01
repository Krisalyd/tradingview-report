from time import sleep
from random import uniform

def custom_delay() -> None:
    """Pause the execution for a random duration between 3 to 8 seconds."""
    sleep(uniform(3, 5))

    