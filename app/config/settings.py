from functools import lru_cache
from typing import List

from decouple import config
from loguru import logger
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_VERSION = config("APP_VERSION", default="0.0.1")
    ENVIRONMENT = config("ENVIRONMENT", default="local")
    TESTING = config("TESTING", default=False)
    APP_PORT = config("APP_PORT", default=8000, cast=int)
    APP_ROOT_PATH = config("APP_ROOT_PATH", default="/")
    APP_NAME = config("APP_NAME", default="Rick and Morty API")
    APP_DESCRIPTION = config("APP_DESCRIPTION", default="Serviço para  disponibilizar dados do seriado RICK and Morty")
    DB_TEST_URL = config("DB_TEST_URL")
    DB_URL = config("DB_URL")
    GENERATE_SCHEMAS = config("GENERATE_SCHEMAS")
    SECRET_KEY = config("SECRET_KEY")
    APP_WORKER = config("APP_WORKER", default=1, cast=int)


    ALLOW_HEADERS: List = ["*"]
    ALLOW_METHODS: List = ["*"]
    ORIGINS: List = [
        "http://localhost",
        "http://localhost:8080",
    ]
    MODELS: List = [
        "aerich.models",
        "app.modules.character.model",
    ]


@lru_cache()
def get_settings():
    logger.info("Loading Config Application")
    return Settings()
