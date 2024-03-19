from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_host: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

try:
    print("Values Fetched from ENV file.")
    settings = Settings()
except Exception as e:
    print(f"Error loading settings: {e}")
    settings = None