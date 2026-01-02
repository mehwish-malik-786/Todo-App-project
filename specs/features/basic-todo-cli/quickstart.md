# Quickstart Guide: Phase I - In-Memory Python Console Todo Application

## Prerequisites
- Python 3.13+ installed on your system

## Running the Application

1. Navigate to the project root directory:
   ```bash
   cd /path/to/todo-app
   ```

2. Run the application:
   ```bash
   python src/main.py
   ```

## Available Commands

Once the application is running, you can use the following commands:

- `add "task title" [optional description]` - Add a new task
- `list` - View all tasks
- `update <id> "new title" [optional new description]` - Update a task
- `delete <id>` - Delete a task
- `complete <id>` - Mark a task as complete
- `incomplete <id>` - Mark a task as incomplete
- `help` - Show available commands
- `quit` or `exit` - Exit the application

## Example Usage

```
> add "Buy groceries" "Milk, bread, eggs"
Task #1 added: Buy groceries

> add "Finish report"
Task #2 added: Finish report

> list
[ ] #1: Buy groceries - Milk, bread, eggs
[ ] #2: Finish report

> complete 1
Task #1 marked as complete

> list
[x] #1: Buy groceries - Milk, bread, eggs
[ ] #2: Finish report

> update 2 "Finish project report" "Complete the quarterly project report"
Task #2 updated

> delete 2
Task #2 deleted

> list
[x] #1: Buy groceries - Milk, bread, eggs

> quit
```

## Error Handling

The application will display clear error messages for invalid inputs:

- `Error: Task with ID <id> does not exist`
- `Error: Invalid command. Type 'help' for available commands`
- `Error: Title cannot be empty`