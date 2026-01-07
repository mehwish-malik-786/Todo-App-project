@echo off
set DATABASE_URL=postgresql://neondb_owner:npg_U86eLxmp@ep-frosty-meadow-aguki2ua-pooler.c-2.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
set BETTER_AUTH_SECRET=fTO4F8akbhKeU8zlyademeM6SN9tdaFR
uvicorn main:app --reload --port 8000