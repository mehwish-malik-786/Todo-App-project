# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Todo App API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and create database tables
from app.models import task
task.create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Todo App API - Phase II"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Include API routes
from app.routes import tasks
app.include_router(tasks.router, prefix="/api", tags=["tasks"])