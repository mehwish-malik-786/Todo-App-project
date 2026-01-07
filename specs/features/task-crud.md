# Feature Specification: Task CRUD Operations

## Overview
This specification defines the Create, Read, Update, and Delete (CRUD) operations for tasks in the Todo App. All operations will be secured using JWT-based authentication, with user identification derived from the JWT token rather than from URL parameters.

## Requirements

### 1. API Endpoints
All endpoints will be under `/api/tasks` and will use the authenticated user's identity from the JWT token for authorization.

### 2. GET /api/tasks - List Tasks
- **Purpose**: Retrieve all tasks for the current authenticated user
- **Authentication**: JWT token required in Authorization header
- **Query Parameters**:
  - `status` (optional): Filter tasks by status (e.g., "all", "active", "completed")
  - `sort` (optional): Sort tasks by criteria (e.g., "created_at", "updated_at", "title")
- **Response**: JSON array of task objects
- **Authorization**: Only returns tasks belonging to the authenticated user

### 3. POST /api/tasks - Create Task
- **Purpose**: Create a new task for the current authenticated user
- **Authentication**: JWT token required in Authorization header
- **Request Body**:
  ```json
  {
    "title": "string (required, 1-200 characters)",
    "description": "string (optional)"
  }
  ```
- **Validation**:
  - Title must be between 1-200 characters
  - Title is required
- **Response**: JSON object of the created task with all fields

### 4. PUT /api/tasks/{id} - Update Task
- **Purpose**: Update an existing task for the current authenticated user
- **Authentication**: JWT token required in Authorization header
- **URL Parameter**: `id` - the unique identifier of the task
- **Request Body**:
  ```json
  {
    "title": "string (required, 1-200 characters)",
    "description": "string (optional)"
  }
  ```
- **Validation**:
  - User must be the owner of the task
  - Title must be between 1-200 characters
  - Title is required
- **Response**: JSON object of the updated task with all fields

### 5. DELETE /api/tasks/{id} - Delete Task
- **Purpose**: Delete an existing task for the current authenticated user
- **Authentication**: JWT token required in Authorization header
- **URL Parameter**: `id` - the unique identifier of the task
- **Validation**: User must be the owner of the task
- **Response**: Empty response with HTTP 204 status

### 6. PATCH /api/tasks/{id}/complete - Toggle Task Completion
- **Purpose**: Toggle the completion status of a task for the current authenticated user
- **Authentication**: JWT token required in Authorization header
- **URL Parameter**: `id` - the unique identifier of the task
- **Validation**: User must be the owner of the task
- **Response**: JSON object of the updated task with completion status changed

## Task Object Structure
All responses will include task objects with the following structure:

```json
{
  "id": "string - unique identifier for the task",
  "title": "string - task title (1-200 characters)",
  "description": "string - optional task description",
  "completed": "boolean - completion status",
  "user_id": "string - reference to the authenticated user",
  "created_at": "string - ISO 8601 timestamp of creation",
  "updated_at": "string - ISO 8601 timestamp of last update"
}
```

## Validation Rules
- **Title**: Required, 1-200 characters
- **Description**: Optional, any length
- **User Ownership**: All operations validate that the authenticated user owns the task
- **Task Existence**: All operations validate that the task exists before performing operations

## Error Handling
- **401 Unauthorized**: JWT token missing or invalid
- **403 Forbidden**: User is not authorized to access the requested task
- **404 Not Found**: Task with the specified ID does not exist
- **422 Unprocessable Entity**: Request body validation failed (e.g., title too long/short)
- **500 Internal Server Error**: Unexpected server error

## Security Considerations
- All endpoints require valid JWT authentication
- User isolation: users can only access their own tasks
- Input validation to prevent injection attacks
- Proper error responses without exposing sensitive information

## Implementation Notes
- The user_id should be extracted from the JWT token, not from URL parameters
- Database queries must filter by the authenticated user's ID
- Timestamps should be stored in UTC
- Use proper database transactions where necessary

## Success Criteria
- All CRUD operations work as specified
- User isolation is properly enforced
- Validation rules are correctly implemented
- Error handling works as specified
- All endpoints return appropriate HTTP status codes
- Response format matches the specified structure