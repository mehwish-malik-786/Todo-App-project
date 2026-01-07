# Feature Specification: JWT-Based Authentication

## Overview
This specification defines the JWT-based authentication system for Phase II of the Todo App. The system will use Better Auth for Next.js with JWT plugin enabled, ensuring secure user authentication and authorization across all API endpoints.

## Requirements

### 1. Better Auth Setup
- Integrate Better Auth into the Next.js frontend with JWT plugin enabled
- Configure Better Auth to use the shared BETTER_AUTH_SECRET for token signing/verification
- Support standard authentication flows: sign up, sign in, sign out
- Implement password reset functionality

### 2. Frontend Authentication Handling
- Store JWT in secure httpOnly cookies to prevent XSS attacks
- Automatically attach JWT to API calls via `Authorization: Bearer <token>` header
- Implement token refresh mechanism to handle token expiration
- Handle authentication errors gracefully with appropriate UI feedback
- Redirect unauthenticated users to login page when accessing protected routes

### 3. Backend Authentication Middleware
- Implement FastAPI middleware to verify JWT using shared secret BETTER_AUTH_SECRET
- Decode and validate JWT tokens on each authenticated request
- Extract user information from the token for request context
- Return appropriate error responses for invalid/missing tokens

### 4. User Model
- User model with the following fields:
  - `id` (string): Unique identifier for the user (managed by Better Auth)
  - `email` (string): User's email address (managed by Better Auth)
- Ensure user data is properly validated and sanitized
- Implement user retrieval by ID for authorization checks

### 5. API Endpoint Protection
- All `/api/` endpoints require a valid JWT token
- Return HTTP 401 Unauthorized if token is missing or invalid
- Implement proper error responses for authentication failures
- Ensure endpoints verify user identity before processing requests

### 6. Task Ownership and User Isolation
- Every task must have a `user_id` (string) field referencing the authenticated user
- Implement database-level user isolation to prevent unauthorized access
- Ensure users can only access, modify, or delete their own tasks
- Validate user ownership before performing any task operations

## Implementation Details

### Frontend Implementation
- Use Better Auth's React hooks for authentication state management
- Implement secure cookie handling using httpOnly cookies
- Create an API client utility that automatically attaches the Authorization header
- Implement error handling for authentication failures
- Create protected route components that check authentication status

### Backend Implementation
- Create a JWT middleware class/function for token validation
- Implement user dependency injection to access user context in endpoints
- Create database models with proper user associations
- Implement authorization checks in service layer
- Ensure all database queries are user-isolated

### Security Considerations
- Use HTTPS in production to prevent token interception
- Implement proper token expiration and refresh mechanisms
- Sanitize all user inputs to prevent injection attacks
- Ensure proper CORS configuration for API endpoints
- Implement rate limiting to prevent brute force attacks

## Error Handling
- Return HTTP 401 for unauthorized requests
- Return HTTP 403 for insufficient permissions
- Provide clear error messages without exposing sensitive information
- Log authentication failures for security monitoring

## Testing Requirements
- Unit tests for JWT token validation
- Integration tests for protected endpoints
- End-to-end tests for authentication flows
- Test user isolation to ensure data security

## Dependencies
- Better Auth for Next.js
- FastAPI for backend framework
- SQLModel for database modeling
- JWT libraries for token handling
- Neon Serverless PostgreSQL for database

## Success Criteria
- Users can sign up, sign in, and sign out securely
- JWT tokens are properly validated on all API endpoints
- Users can only access their own tasks
- Authentication state is properly maintained across the application
- All security requirements are met
- Tests pass for all authentication functionality