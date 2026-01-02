"""
Command-line interface for the Todo App
"""
import sys
from typing import List
try:
    from .todo_app import TodoList, Task, TaskStatus
except ImportError:
    from todo_app import TodoList, Task, TaskStatus


class TodoCLI:
    """Command-line interface for interacting with the TodoList"""
    
    def __init__(self):
        self.todo_list = TodoList()
    
    def display_help(self):
        """Display help information for available commands"""
        help_text = """
Todo App - Command Line Interface
=================================

Available commands:
  add <title> [description]     - Add a new task
  list                          - List all tasks
  update <id> <title> [desc]    - Update a task
  delete <id>                   - Delete a task
  complete <id>                 - Mark task as complete
  incomplete <id>               - Mark task as incomplete
  help                          - Show this help message
  quit/exit                     - Exit the application

Examples:
  add "Buy groceries" "Milk, bread, eggs"
  list
  complete 1
  update 2 "Updated title" "Updated description"
  delete 3
        """
        print(help_text)
    
    def parse_command(self, user_input: str) -> List[str]:
        """
        Parse user input into command and arguments
        Handles quoted strings as single arguments
        
        Args:
            user_input: Raw user input string
            
        Returns:
            List of parsed command and arguments
        """
        # Simple parsing that handles quoted strings
        parts = []
        current_part = ""
        in_quotes = False
        quote_char = None
        
        i = 0
        while i < len(user_input):
            char = user_input[i]
            
            if char in ['"', "'"] and not in_quotes:
                in_quotes = True
                quote_char = char
            elif char == quote_char and in_quotes:
                in_quotes = False
                quote_char = None
                # Don't add the quote character to the part
            elif char == ' ' and not in_quotes:
                if current_part:
                    parts.append(current_part)
                    current_part = ""
            else:
                current_part += char
            
            i += 1
        
        # Add the last part if it exists
        if current_part:
            parts.append(current_part)
        
        return parts
    
    def handle_add(self, args: List[str]) -> bool:
        """Handle the 'add' command"""
        if len(args) < 2:
            print("Error: 'add' command requires a title")
            print("Usage: add <title> [description]")
            return True
        
        title = args[1]
        description = " ".join(args[2:]) if len(args) > 2 else None
        
        try:
            task = self.todo_list.add_task(title, description)
            print(f"Added task #{task.id}: {task.title}")
            if task.description:
                print(f"  Description: {task.description}")
        except ValueError as e:
            print(f"Error: {e}")
        
        return True
    
    def handle_list(self, args: List[str]) -> bool:
        """Handle the 'list' command"""
        tasks = self.todo_list.get_all_tasks()
        
        if not tasks:
            print("No tasks in the list.")
            return True
        
        print("\nTodo List:")
        print("----------")
        for task in tasks:
            status = "✓" if task.status == TaskStatus.COMPLETE else "○"
            print(f"{status} [{task.id}] {task.title}")
            if task.description:
                print(f"      Description: {task.description}")
        print()
        
        return True
    
    def handle_update(self, args: List[str]) -> bool:
        """Handle the 'update' command"""
        if len(args) < 3:
            print("Error: 'update' command requires an ID and a new title")
            print("Usage: update <id> <title> [description]")
            return True
        
        try:
            task_id = int(args[1])
        except ValueError:
            print("Error: Task ID must be a number")
            return True
        
        title = args[2]
        description = " ".join(args[3:]) if len(args) > 3 else None
        
        try:
            updated = self.todo_list.update_task(task_id, title, description)
            if updated:
                print(f"Updated task #{task_id}")
            else:
                print(f"Error: Task with ID {task_id} not found")
        except ValueError as e:
            print(f"Error: {e}")
        
        return True
    
    def handle_delete(self, args: List[str]) -> bool:
        """Handle the 'delete' command"""
        if len(args) < 2:
            print("Error: 'delete' command requires an ID")
            print("Usage: delete <id>")
            return True
        
        try:
            task_id = int(args[1])
        except ValueError:
            print("Error: Task ID must be a number")
            return True
        
        deleted = self.todo_list.delete_task(task_id)
        if deleted:
            print(f"Deleted task #{task_id}")
        else:
            print(f"Error: Task with ID {task_id} not found")
        
        return True
    
    def handle_complete(self, args: List[str]) -> bool:
        """Handle the 'complete' command"""
        if len(args) < 2:
            print("Error: 'complete' command requires an ID")
            print("Usage: complete <id>")
            return True
        
        try:
            task_id = int(args[1])
        except ValueError:
            print("Error: Task ID must be a number")
            return True
        
        completed = self.todo_list.mark_task_complete(task_id)
        if completed:
            print(f"Marked task #{task_id} as complete")
        else:
            print(f"Error: Task with ID {task_id} not found")
        
        return True
    
    def handle_incomplete(self, args: List[str]) -> bool:
        """Handle the 'incomplete' command"""
        if len(args) < 2:
            print("Error: 'incomplete' command requires an ID")
            print("Usage: incomplete <id>")
            return True
        
        try:
            task_id = int(args[1])
        except ValueError:
            print("Error: Task ID must be a number")
            return True
        
        marked = self.todo_list.mark_task_incomplete(task_id)
        if marked:
            print(f"Marked task #{task_id} as incomplete")
        else:
            print(f"Error: Task with ID {task_id} not found")
        
        return True
    
    def run(self):
        """Run the command-line interface"""
        print("Welcome to the Todo App!")
        print("Type 'help' for available commands or 'quit' to exit.\n")
        
        while True:
            try:
                user_input = input("> ").strip()
                
                if not user_input:
                    continue
                
                # Parse the command
                args = self.parse_command(user_input)
                command = args[0].lower()
                
                # Handle different commands
                if command in ['quit', 'exit']:
                    print("Goodbye!")
                    break
                elif command == 'help':
                    self.display_help()
                elif command == 'add':
                    self.handle_add(args)
                elif command == 'list':
                    self.handle_list(args)
                elif command == 'update':
                    self.handle_update(args)
                elif command == 'delete':
                    self.handle_delete(args)
                elif command == 'complete':
                    self.handle_complete(args)
                elif command == 'incomplete':
                    self.handle_incomplete(args)
                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' for available commands")
            
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break