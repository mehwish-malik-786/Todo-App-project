# backend/app/models/task.py
from sqlmodel import SQLModel, Field, create_engine, Session, select
from datetime import datetime
from typing import Optional
import os
from sqlmodel import SQLModel, Field
from datetime import datetime

class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None, max_length=None)
    completed: bool = Field(default=False)
    user_id: str = Field(nullable=False)  # Foreign key to Better Auth users.id

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# Import this in main.py to create tables
def create_db_and_tables():
    from app.database import engine
    SQLModel.metadata.create_all(engine)