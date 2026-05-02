from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/skwirel"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    CLERK_PUBLISHABLE_KEY: str = ""
    CLERK_SECRET_KEY: str = ""
    CLERK_JWT_ALGORITHM: str = "HS256"
    DEV_AUTH_MODE: bool = True
    DEV_USER_ID: str = "dev_user_123"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
