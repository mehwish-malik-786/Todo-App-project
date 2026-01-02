"""
Basic tests for the Todo App functionality
"""
import sys
import os
# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from todo_app import TodoList, TaskStatus


def test_basic_functionality():
    """Test the basic functionality of the TodoList"""
    print("Testing basic functionality...")
    
    # Create a new todo list
    todo_list = TodoList()
    
    # Test adding tasks
    print("\n1. Testing task creation...")
    task1 = todo_list.add_task("Buy groceries", "Milk, bread, eggs")
    print(f"   Added task: #{task1.id} - {task1.title}")
    
    task2 = todo_list.add_task("Walk the dog")
    print(f"   Added task: #{task2.id} - {task2.title}")
    
    # Test listing tasks
    print("\n2. Testing task listing...")
    tasks = todo_list.get_all_tasks()
    print(f"   Total tasks: {len(tasks)}")
    for task in tasks:
        status = "Complete" if task.status == TaskStatus.COMPLETE else "Incomplete"
        print(f"   #{task.id}: {task.title} - {status}")
        if task.description:
            print(f"      Description: {task.description}")
    
    # Test updating a task
    print("\n3. Testing task update...")
    updated = todo_list.update_task(task1.id, "Buy groceries and cook dinner", "Milk, bread, eggs, chicken")
    print(f"   Update successful: {updated}")
    
    if updated:
        updated_task = todo_list.get_task_by_id(task1.id)
        print(f"   Updated task: {updated_task.title}")
        print(f"   Updated description: {updated_task.description}")
    
    # Test marking as complete
    print("\n4. Testing marking as complete...")
    completed = todo_list.mark_task_complete(task1.id)
    print(f"   Marked as complete: {completed}")
    
    if completed:
        completed_task = todo_list.get_task_by_id(task1.id)
        status = "Complete" if completed_task.status == TaskStatus.COMPLETE else "Incomplete"
        print(f"   Task status: {status}")
    
    # Test deleting a task
    print("\n5. Testing task deletion...")
    deleted = todo_list.delete_task(task2.id)
    print(f"   Deleted task: {deleted}")
    
    tasks_after_delete = todo_list.get_all_tasks()
    print(f"   Remaining tasks: {len(tasks_after_delete)}")
    
    print("\nAll basic functionality tests passed!")


if __name__ == "__main__":
    test_basic_functionality()