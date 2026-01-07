# Phase II: Full-Stack Web Application Constitution

## Core Principles

### Monorepo Architecture
This is a monorepo with `/frontend` (Next.js 14 App Router) and `/backend` (FastAPI + SQLModel). All components must work cohesively while maintaining clear separation of concerns.

### Authentication-First Design
Authentication must use Better Auth (Next.js) with JWT tokens. Security is paramount and must be implemented at the foundation level, not as an afterthought.

### Database-Driven Isolation
Database must be Neon Serverless PostgreSQL with user-isolation enforced at the database level. All data access must be properly scoped to the authenticated user.

### API-First Development
All API endpoints must be user-isolated based on JWT user_id. The API layer must provide clean, consistent interfaces for frontend consumption.

### Spec-Driven Implementation
No manual coding: all implementation must flow from specs in `/specs/`. This ensures reproducible excellence and traceable development.

### Future-Proof Design
Future compatibility: APIs must be simple JSON for AI agent integration (Phase III). Design decisions must consider the next phase of development.

## Key Standards

### Tech Stack Compliance
- Frontend: Next.js 14 with App Router
- Backend: FastAPI + SQLModel
- Authentication: Better Auth
- Database: Neon Serverless PostgreSQL
- Environment Management: Environment variables for secrets

### Authentication & Security
- JWT-based authentication with proper token validation
- User data isolation enforced at both API and database layers
- Secure handling of authentication tokens
- Proper session management

### Database Design
- Serverless PostgreSQL with connection pooling
- User-isolated data access patterns
- Proper indexing and query optimization
- SQLModel for database schema management

### API Design
- RESTful endpoints with consistent naming conventions
- User-isolated endpoints using JWT user_id
- Proper error handling and response formatting
- Simple JSON responses for AI agent compatibility

### Environment Configuration
- BETTER_AUTH_SECRET (shared between frontend and backend)
- DATABASE_URL (Neon Serverless PostgreSQL)
- Proper environment variable management across both frontend and backend

## Constraints

- Zero Manual Code: All code must be generated from specifications
- User Isolation: Every endpoint must enforce user isolation
- JWT Compliance: All authenticated endpoints must validate JWT tokens
- Monorepo Structure: Frontend and backend must coexist in single repository
- Spec Completeness: Every feature must be spec'd before implementation

## Success Criteria

A Phase II implementation is successful only when all of the following are true:

✅ Next.js 14 frontend with App Router properly configured
✅ FastAPI backend with SQLModel integration
✅ Better Auth authentication system working end-to-end
✅ Neon Serverless PostgreSQL database with user isolation
✅ All API endpoints properly isolated by user_id
✅ Environment variables properly configured and secured
✅ Frontend and backend communicating securely
✅ Simple JSON API responses compatible with AI agents
✅ All functionality spec'd in `/specs/` before implementation

## Governance

This constitution governs Phase II: Full-Stack Web Application development. All development activities for this phase must align with the principles and standards outlined above. This document serves as the foundation for all spec creation and implementation during Phase II.

**Version**: 1.0.0 | **Ratified**: 2026-01-07 | **Phase**: II