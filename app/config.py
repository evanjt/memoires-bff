from pydantic_settings import BaseSettings
from functools import lru_cache


class Config(BaseSettings):
    API_PREFIX: str = "/api"

    # MEMOIRES-API settings
    MEMOIRES_API_URL: (
        str  # Full path to the Memoires API (eg: http://memoires-api:8000)
    )


@lru_cache()
def get_config():
    return Config()


config = get_config()
