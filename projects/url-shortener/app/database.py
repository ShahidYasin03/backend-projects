from pydantic_settings import BaseSettings, SettingsConfigDict
import psycopg


class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


def get_connection():
    return psycopg.connect(settings.DATABASE_URL)