from dotenv import load_dotenv
import os

load_dotenv()

def get_env_str(key: str) -> str:
    value: str | None
    value = os.getenv(key)
    if value is None:
        raise EnvironmentError(f"{key} is not set.")
    return value
