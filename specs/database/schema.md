# Database Schema Specification: Neon PostgreSQL

## Overview
This specification defines the database schema for the Todo App Phase II, using Neon Serverless PostgreSQL. The schema is designed to support JWT-based authentication with user isolation and to accommodate future enhancements.

## Connection Configuration
- **Database**: Neon Serverless PostgreSQL
- **Connection String**: Use DATABASE_URL environment variable with sslmode=require
- **Example**: `postgresql://neondb_owner:password@ep-frosty-meadow-aguki2ua-pooler.c-2.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require`

## Schema Design Principles
- User isolation: All data access is filtered by user_id
- Performance: Proper indexing for common query patterns
- Extensibility: Designed to accommodate future fields and requirements
- Security: Proper constraints and data validation at database level

## Table: tasks

### Columns
- `id`: SERIAL PRIMARY KEY
  - Auto-incrementing integer identifier for each task
  - Unique identifier for the task record
  - Indexed automatically as primary key

- `user_id`: VARCHAR(255) NOT NULL
  - Foreign key referencing Better Auth users.id
  - Required field to ensure user isolation
  - All queries must filter by this field for security

- `title`: VARCHAR(200) NOT NULL
  - Task title with 1-200 character validation
  - Required field for all tasks
  - Enforced at both application and database level

- `description`: TEXT
  - Optional task description
  - Can be NULL if no description is provided
  - No length restriction to allow for detailed descriptions

- `completed`: BOOLEAN DEFAULT FALSE
  - Task completion status
  - Defaults to FALSE when creating new tasks
  - Used for filtering completed vs active tasks

- `created_at`: TIMESTAMP DEFAULT NOW()
  - Timestamp of when the task was created
  - Automatically set to current time when record is inserted
  - Useful for sorting and tracking task creation

- `updated_at`: TIMESTAMP DEFAULT NOW()
  - Timestamp of when the task was last updated
  - Automatically updated when record is modified
  - Useful for tracking changes and sorting by recency

### Indexes
The following indexes are required for optimal performance:

1. **Index on user_id**:
   - Purpose: Essential for user isolation queries
   - Query pattern: `WHERE user_id = $1`
   - Required for all authenticated user queries

2. **Index on completed**:
   - Purpose: Optimize filtering by completion status
   - Query pattern: `WHERE completed = $1`
   - Required for status-based filtering

3. **Composite index on (user_id, completed)**:
   - Purpose: Optimize queries that filter by both user and status
   - Query pattern: `WHERE user_id = $1 AND completed = $2`
   - Most common query pattern for authenticated users

### Additional Indexes (Future Considerations)
- Index on created_at for chronological sorting
- Index on updated_at for recency-based queries
- Index on due_date when implemented in Phase III

## Constraints
- All tasks must have a valid user_id (foreign key constraint to Better Auth users)
- Title cannot be NULL and must be between 1-200 characters
- Completed field defaults to FALSE
- created_at and updated_at are automatically managed

## Future-Proofing Considerations
The schema is designed to accommodate future enhancements:

- **Phase III Enhancements**:
  - `due_date`: TIMESTAMP NULL - For task deadlines
  - `priority`: INTEGER DEFAULT 0 - For task prioritization
  - `category_id`: INTEGER - For task categorization
  - `parent_task_id`: INTEGER - For hierarchical tasks

- **Additional Considerations**:
  - `deleted_at`: TIMESTAMP NULL - For soft deletes
  - `position`: INTEGER - For custom task ordering
  - `estimated_duration`: INTEGER - For time management

## Security Considerations
- All queries must filter by user_id to ensure data isolation
- No direct access to other users' tasks
- Proper database permissions to prevent unauthorized access
- SSL connection required (sslmode=require)

## Performance Considerations
- Proper indexing as specified above
- Connection pooling for efficient resource usage
- Query optimization for common access patterns
- Regular monitoring of slow queries

## Migration Strategy
- Initial schema creation with all required tables and indexes
- Future migrations for additional fields in subsequent phases
- Proper backup strategy before any schema changes
- Rollback procedures for failed migrations

## Validation
- Database-level constraints to enforce data integrity
- Application-level validation for additional business rules
- Regular testing of user isolation mechanisms
- Performance testing of common query patterns

## Success Criteria
- Schema supports all required functionality for Phase II
- Proper user isolation is enforced at database level
- All required indexes are created for optimal performance
- Connection to Neon PostgreSQL is established with SSL
- Schema is extensible for future phases
- Security requirements are met