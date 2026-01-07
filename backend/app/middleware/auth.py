# backend/app/middleware/auth.py
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from pydantic import BaseModel
import os
import jwt
from datetime import datetime, timedelta
from sqlmodel import Session
from app.database import get_session
from app.models.task import Task

# JWT Configuration
SECRET_KEY = os.getenv("BETTER_AUTH_SECRET")
ALGORITHM = "HS256"

security = HTTPBearer()

class TokenData(BaseModel):
    user_id: str
    email: str

def verify_token(token: str) -> Optional[TokenData]:
    """
    Verify the JWT token and return the user data if valid
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("id")
        email: str = payload.get("email")
        
        if user_id is None or email is None:
            return None
        
        token_data = TokenData(user_id=user_id, email=email)
        return token_data
    except jwt.PyJWTError:
        return None

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_session)
):
    """
    Get the current user from the JWT token
    """
    token_data = verify_token(credentials.credentials)
    
    if token_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return token_data

def get_current_user_id(
    current_user: TokenData = Depends(get_current_user)
) -> str:
    """
    Get the current user's ID from the JWT token
    """
    return current_user.user_id