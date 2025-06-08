from pydantic import BaseModel
import os

class Settings(BaseModel):
    DB_USER: str = os.getenv("DB_USER", "tournament_user")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "qwerty123")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", "5432"))
    DB_NAME: str = os.getenv("DB_NAME", "tournaments_db")

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()
