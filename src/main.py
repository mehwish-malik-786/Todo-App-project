"""
Main entry point for the Todo App
Phase I: In-Memory Python Console Todo Application
"""
try:
    from .cli import TodoCLI
except ImportError:
    from cli import TodoCLI


def main():
    """Main function to run the Todo App CLI"""
    app = TodoCLI()
    app.run()


if __name__ == "__main__":
    main()