# backend/app/database.py
import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session
from typing import Generator

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set")

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

def get_session() -> Generator[Session, None, None]:
    """
    Get a database session
    """
    with Session(engine) as session:
        yield session