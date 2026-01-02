"""
Demonstration script for the Todo App
Shows all the core functionality in action
"""

import sys
import os
# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from todo_app import TodoList, TaskStatus


def demonstrate_features():
    """Demonstrate all the features of the Todo App"""
    print("Todo App - Phase I - Feature Demonstration")
    print("=" * 45)

    # Create a new todo list
    todo_list = TodoList()

    print("\n1. ADDING TASKS")
    print("-" * 20)

    # Add some tasks
    task1 = todo_list.add_task("Buy groceries", "Milk, bread, eggs, cheese")
    print(f"[OK] Added task #{task1.id}: {task1.title}")

    task2 = todo_list.add_task("Walk the dog", "Don't forget the leash")
    print(f"[OK] Added task #{task2.id}: {task2.title}")

    task3 = todo_list.add_task("Finish report")
    print(f"[OK] Added task #{task3.id}: {task3.title}")

    print("\n2. LISTING TASKS")
    print("-" * 20)

    # List all tasks
    tasks = todo_list.get_all_tasks()
    print(f"Total tasks: {len(tasks)}")
    for task in tasks:
        status = "[Complete]" if task.status == TaskStatus.COMPLETE else "[Incomplete]"
        print(f"  {status} [{task.id}] {task.title}")
        if task.description:
            print(f"        Description: {task.description}")

    print("\n3. UPDATING TASKS")
    print("-" * 20)

    # Update a task
    updated = todo_list.update_task(task1.id, "Buy groceries and cook dinner", "Milk, bread, eggs, cheese, chicken")
    if updated:
        print(f"[OK] Updated task #{task1.id}")
        updated_task = todo_list.get_task_by_id(task1.id)
        print(f"  New title: {updated_task.title}")
        print(f"  New description: {updated_task.description}")

    print("\n4. MARKING TASKS AS COMPLETE")
    print("-" * 30)

    # Mark a task as complete
    completed = todo_list.mark_task_complete(task2.id)
    if completed:
        print(f"[OK] Marked task #{task2.id} as complete")
        completed_task = todo_list.get_task_by_id(task2.id)
        status = "[Complete]" if completed_task.status == TaskStatus.COMPLETE else "[Incomplete]"
        print(f"  Status: {status}")

    print("\n5. LISTING TASKS AFTER CHANGES")
    print("-" * 30)

    # List all tasks again to show changes
    tasks = todo_list.get_all_tasks()
    print(f"Total tasks: {len(tasks)}")
    for task in tasks:
        status = "[Complete]" if task.status == TaskStatus.COMPLETE else "[Incomplete]"
        print(f"  {status} [{task.id}] {task.title}")

    print("\n6. DELETING A TASK")
    print("-" * 20)

    # Delete a task
    deleted = todo_list.delete_task(task3.id)
    if deleted:
        print(f"[OK] Deleted task #{task3.id}")

    # Show remaining tasks
    tasks = todo_list.get_all_tasks()
    print(f"Remaining tasks: {len(tasks)}")
    for task in tasks:
        status = "[Complete]" if task.status == TaskStatus.COMPLETE else "[Incomplete]"
        print(f"  {status} [{task.id}] {task.title}")

    print("\n7. ERROR HANDLING")
    print("-" * 20)

    # Try to update a non-existent task
    updated = todo_list.update_task(999, "Non-existent task")
    print(f"[OK] Attempt to update non-existent task handled: {updated}")

    # Try to delete a non-existent task
    deleted = todo_list.delete_task(999)
    print(f"[OK] Attempt to delete non-existent task handled: {deleted}")

    print("\n" + "=" * 45)
    print("DEMONSTRATION COMPLETE")
    print("All core features of the Todo App have been demonstrated!")
    print("The application successfully handles:")
    print("- Adding tasks with titles and descriptions")
    print("- Listing all tasks with status indicators")
    print("- Updating task information")
    print("- Marking tasks as complete/incomplete")
    print("- Deleting tasks")
    print("- Error handling for invalid operations")


if __name__ == "__main__":
    demonstrate_features()