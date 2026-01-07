# backend/app/routes/tasks.py
from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from sqlmodel import Session, select
from datetime import datetime
from app.database import get_session
from app.models.task import Task, TaskBase
from app.middleware.auth import get_current_user_id

router = APIRouter()

@router.get("/tasks", response_model=List[Task])
def get_tasks(
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session),
    status_param: Optional[str] = Query(None, alias="status"),
    sort: Optional[str] = Query(None)
):
    """
    Get all tasks for the current user
    """
    query = select(Task).where(Task.user_id == current_user_id)
    
    # Apply status filter if provided
    if status_param:
        if status_param == "active":
            query = query.where(Task.completed == False)
        elif status_param == "completed":
            query = query.where(Task.completed == True)
    
    # Apply sorting if provided
    if sort == "created_at":
        query = query.order_by(Task.created_at)
    elif sort == "updated_at":
        query = query.order_by(Task.updated_at)
    elif sort == "title":
        query = query.order_by(Task.title)
    
    tasks = session.exec(query).all()
    return tasks


@router.post("/tasks", response_model=Task)
def create_task(
    task_data: TaskBase,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    """
    Create a new task for the current user
    """
    task = Task(
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed,
        user_id=current_user_id
    )
    
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task


@router.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task_data: TaskBase,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    """
    Update an existing task for the current user
    """
    # Verify that the task belongs to the current user
    task = session.get(Task, task_id)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    if task.user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this task"
        )
    
    # Update the task
    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed
    task.updated_at = datetime.utcnow()
    
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    """
    Delete a task for the current user
    """
    # Verify that the task belongs to the current user
    task = session.get(Task, task_id)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    if task.user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this task"
        )
    
    session.delete(task)
    session.commit()
    
    return {"message": "Task deleted successfully"}


@router.patch("/tasks/{task_id}/complete", response_model=Task)
def toggle_task_completion(
    task_id: int,
    current_user_id: str = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    """
    Toggle the completion status of a task for the current user
    """
    # Verify that the task belongs to the current user
    task = session.get(Task, task_id)
    
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    if task.user_id != current_user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to modify this task"
        )
    
    # Toggle the completion status
    task.completed = not task.completed
    task.updated_at = datetime.utcnow()
    
    session.add(task)
    session.commit()
    session.refresh(task)
    
    return task