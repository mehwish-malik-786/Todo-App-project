# Todo App - Phase I

This is an in-memory Python console todo application that stores tasks in memory.

## Features

- Add tasks with titles and optional descriptions
- List all tasks with their status
- Update task titles and descriptions
- Delete tasks
- Mark tasks as complete/incomplete
- Command-line interface for easy interaction

## How to Run

To run the application, execute:

```bash
python -m src.main
```

## Available Commands

- `add <title> [description]` - Add a new task
- `list` - List all tasks
- `update <id> <title> [desc]` - Update a task
- `delete <id>` - Delete a task
- `complete <id]` - Mark task as complete
- `incomplete <id]` - Mark task as incomplete
- `help` - Show help information
- `quit/exit` - Exit the application

## Examples

```
> add "Buy groceries" "Milk, bread, eggs"
Added task #1: Buy groceries

> list
Todo List:
----------
○ [1] Buy groceries
      Description: Milk, bread, eggs

> complete 1
Marked task #1 as complete

> list
Todo List:
----------
✓ [1] Buy groceries
      Description: Milk, bread, eggs

> quit
Goodbye!
```

## Architecture

The application consists of three main components in the `src` directory:

1. `src/todo_app.py` - Contains the core business logic with Task and TodoList classes
2. `src/cli.py` - Provides the command-line interface
3. `src/main.py` - Entry point for the application

## Constraints

- All data is stored in memory only (no persistence)
- Built with Python 3.13+ standard library only (no external dependencies)
- Follows the specification in `specs/features/basic-todo-cli.md`