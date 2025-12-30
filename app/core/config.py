from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # matches your .env key DATABASE_URL
    database_url: str

    # matches your .env keys
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    access_token_exp_minutes: int = 60

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
