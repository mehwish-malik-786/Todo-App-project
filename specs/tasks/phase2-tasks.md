# Phase II Atomic Tasks

## Task List

- Task 1: Create monorepo structure (frontend/, backend/, specs/) — @specs/plans/phase2-plan.md#1
- Task 2: Set up Next.js 14 app with Tailwind — @specs/plans/phase2-plan.md#2
- Task 3: Configure Better Auth with JWT — @specs/features/authentication.md
- Task 4: Create FastAPI app with SQLModel — @specs/plans/phase2-plan.md#4
- Task 5: Implement JWT middleware — @specs/features/authentication.md
- Task 6: Define Task model and CRUD routes — @specs/features/task-crud.md + @specs/database/schema.md
- Task 7: Build Next.js task UI — @specs/features/task-crud.md
- Task 8: Create API client with JWT auto-attach — @specs/features/authentication.md

## Detailed Task Descriptions

### Task 1: Create monorepo structure (frontend/, backend/, specs/)
- Create frontend directory with basic Next.js structure
- Create backend directory with basic FastAPI structure  
- Create specs directory with subdirectories (database, features, plans, tasks)
- Set up root-level configuration files
- Configure .gitignore to exclude sensitive files and build artifacts

### Task 2: Set up Next.js 14 app with Tailwind
- Initialize Next.js 14 project using create-next-app or manually
- Configure App Router for page routing
- Install and configure Tailwind CSS for styling
- Set up basic layout and global styles
- Create reusable UI components (Button, Card, Input, etc.)

### Task 3: Configure Better Auth with JWT
- Install Better Auth package in the frontend
- Configure authentication providers (email, social logins)
- Set up JWT plugin for token-based authentication
- Configure BETTER_AUTH_SECRET from environment variables
- Implement login, signup, and logout functionality
- Create protected route components

### Task 4: Create FastAPI app with SQLModel
- Initialize FastAPI application
- Install and configure SQLModel for database modeling
- Set up database connection to Neon Serverless PostgreSQL
- Configure connection pooling and SSL settings
- Create database session management utilities
- Implement basic API router structure

### Task 5: Implement JWT middleware
- Create JWT verification middleware for FastAPI
- Use BETTER_AUTH_SECRET to validate tokens from Better Auth
- Extract user information from JWT payload
- Create dependency to inject user context into endpoints
- Implement proper error responses for authentication failures
- Test middleware with various token scenarios

### Task 6: Define Task model and CRUD routes
- Create Task model using SQLModel with fields from database schema
- Implement database operations (create, read, update, delete)
- Create API routes for /api/tasks endpoints:
  - GET /api/tasks - list tasks with filtering and sorting
  - POST /api/tasks - create new task
  - PUT /api/tasks/{id} - update task
  - DELETE /api/tasks/{id} - delete task
  - PATCH /api/tasks/{id}/complete - toggle completion status
- Implement user isolation at database and API levels
- Add proper validation and error handling

### Task 7: Build Next.js task UI
- Create login page with authentication forms
- Build dashboard page with task list component
- Implement add/edit task form with validation
- Create task item components with delete/complete buttons
- Add filtering and sorting functionality to task list
- Implement responsive design for different screen sizes
- Add loading states and error handling UI

### Task 8: Create API client with JWT auto-attach
- Create API client utility in frontend/lib/api.ts
- Implement automatic JWT token attachment to requests
- Handle authentication errors and redirect to login
- Create wrapper functions for each API endpoint
- Implement proper error handling and user feedback
- Ensure type safety with TypeScript interfaces