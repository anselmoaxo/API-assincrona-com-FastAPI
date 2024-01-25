from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://postgres:postgres@localhost:5433/Workout')


settings = Settings()