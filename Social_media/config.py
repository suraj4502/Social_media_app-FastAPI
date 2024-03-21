from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = "Social_media/.env"

try:
    settings = Settings()
    print("Values Fetched from ENV file.")
except Exception as e:
    print(f"Error loading settings: {e}")
    settings = None