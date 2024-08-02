import os
from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    database_url: str = Field(..., env="DATABASE_URL")
    postgres_username: str = Field(..., env="POSTGRES_USERNAME")
    postgres_password: str = Field(..., env="POSTGRES_PASSWORD")
    db_name: str = Field(..., env="DB_NAME")
    mail_username: str = Field(..., env="MAIL_USERNAME")
    mail_password: str = Field(..., env="MAIL_PASSWORD")
    mail_server: str = Field(..., env="MAIL_SERVER")
    mail_port: int = Field(..., env="MAIL_PORT")
    mail_from: str = Field(..., env="MAIL_FROM")
    secret_key: str = Field(..., env="SECRET_KEY")
    algorithm: str = Field(..., env="ALGORITHM")
    access_token_expire_minutes: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")
    refresh_token_expire_days: int = Field(..., env="REFRESH_TOKEN_EXPIRE_DAYS")
    mail_starttls: bool = Field(..., env="MAIL_STARTTLS")
    mail_ssl_tls: bool = Field(..., env="MAIL_SSL_TLS")

    model_config = {
        "env_file": ".env",
        "extra": "allow"  # Allow extra fields, though not generally recommended
    }

# Initialize the settings object
settings = Settings()

# Print the loaded settings for verification
print("Settings loaded:", settings.model_dump())
