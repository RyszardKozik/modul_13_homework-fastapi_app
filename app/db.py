from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os
from app.config import settings

# Load environment variables from .env file
load_dotenv("../.env")  
print(os.getenv("DATABASE_URL"))

# Read database URL from environment variables
class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

if not settings.DATABASE_URL:
    raise ValueError("No DATABASE_URL set for SQLAlchemy database")

# Create the SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for our models to inherit from
Base = declarative_base()

# Dependency for getting the database session
def get_db():
    """
    Dependency for getting the database session.

    Yields:
        Session: A new database session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
