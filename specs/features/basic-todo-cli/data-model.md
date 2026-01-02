# Data Model: Phase I - In-Memory Python Console Todo Application

## Task Entity

### Attributes
- **id**: `int` (unique identifier, auto-incrementing starting from 1)
- **title**: `str` (required, non-empty string)
- **description**: `str` (optional, can be empty string)
- **completed**: `bool` (default: False)

### Validation Rules
- `id` must be a positive integer
- `title` must be a non-empty string (1+ characters)
- `completed` must be a boolean value

### State Transitions
- A task can transition from `completed=False` to `completed=True` (mark as complete)
- A task can transition from `completed=True` to `completed=False` (mark as incomplete)

## TodoList Collection

### Operations
- **Add Task**: Creates a new task with auto-generated ID and `completed=False`
- **View Tasks**: Returns all tasks in the collection
- **Update Task**: Modifies the title or description of a task by ID
- **Delete Task**: Removes a task from the collection by ID
- **Mark Complete/Incomplete**: Changes the completion status of a task by ID

### Validation Rules
- Task IDs must be unique within the collection
- Operations targeting a specific task ID must fail gracefully if the ID doesn't exist
- The collection should support up to 1000 tasks in memory