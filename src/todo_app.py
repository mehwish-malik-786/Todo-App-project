"""
Todo App - Phase I Implementation
In-memory Python Console Todo Application
"""

from typing import List, Optional
from dataclasses import dataclass, field
from enum import Enum


class TaskStatus(Enum):
    """Enumeration for task status"""
    INCOMPLETE = "incomplete"
    COMPLETE = "complete"


@dataclass
class Task:
    """Represents a single todo task"""
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.INCOMPLETE


class TodoList:
    """Collection of Task entities that supports add, view, update, delete, and mark operations"""
    
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the todo list
        
        Args:
            title: The title of the task (required)
            description: Optional description of the task
            
        Returns:
            The newly created Task object
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip() if description else None,
            status=TaskStatus.INCOMPLETE
        )
        
        self._tasks.append(task)
        self._next_id += 1
        return task
    
    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the todo list
        
        Returns:
            List of all Task objects
        """
        return self._tasks.copy()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update a task's title or description by its ID
        
        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)
            
        Returns:
            True if the task was updated, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty")
            task.title = title.strip()
        
        if description is not None:
            task.description = description.strip() if description else None
        
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if the task was deleted, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        self._tasks.remove(task)
        return True
    
    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete
        
        Args:
            task_id: The ID of the task to mark as complete
            
        Returns:
            True if the task was marked as complete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.status = TaskStatus.COMPLETE
        return True
    
    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete
        
        Args:
            task_id: The ID of the task to mark as incomplete
            
        Returns:
            True if the task was marked as incomplete, False if task was not found
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        task.status = TaskStatus.INCOMPLETE
        return True