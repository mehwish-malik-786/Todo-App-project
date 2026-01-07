# backend/app/models/user.py
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid
from sqlmodel import create_engine, Session


class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False)
    name: str = Field(nullable=False)


class User(UserBase, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    password_hash: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)
    email_verified: bool = Field(default=False)


# Import this in main.py to create tables
def create_db_and_tables():
    from app.database import engine
    SQLModel.metadata.create_all(engine)