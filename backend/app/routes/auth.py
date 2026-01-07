# backend/app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import BaseModel
from typing import Optional
from sqlmodel import Session, select
from datetime import datetime, timedelta
import jwt
import os
import bcrypt
from app.database import get_session
from app.models.user import User
from app.middleware.auth import SECRET_KEY, ALGORITHM, TokenData, verify_token

router = APIRouter()

# Models for request/response
class UserRegisterRequest(BaseModel):
    email: str
    name: str
    password: str

class UserLoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: str
    created_at: datetime

# Password hashing utility
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Create JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)  # Default 15 minutes
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/register", response_model=UserResponse)
def register(user_data: UserRegisterRequest, session: Session = Depends(get_session)):
    # Check if user already exists
    existing_user = session.exec(select(User).where(User.email == user_data.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    # Hash the password
    hashed_password = hash_password(user_data.password)
    
    # Create new user
    user = User(
        email=user_data.email,
        name=user_data.name,
        password_hash=hashed_password
    )
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return UserResponse(
        id=user.id,
        email=user.email,
        name=user.name,
        created_at=user.created_at
    )

@router.post("/login", response_model=TokenResponse)
def login(user_data: UserLoginRequest, session: Session = Depends(get_session)):
    # Find user by email
    user = session.exec(select(User).where(User.email == user_data.email)).first()
    
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create JWT token
    access_token_expires = timedelta(minutes=30)  # Token valid for 30 minutes
    access_token = create_access_token(
        data={"id": user.id, "email": user.email},
        expires_delta=access_token_expires
    )
    
    return TokenResponse(access_token=access_token, token_type="bearer")

@router.post("/logout")
def logout():
    # In a stateless JWT system, logout is typically handled on the client side
    # by removing the token from storage. This endpoint can be used for additional
    # server-side operations if needed.
    return {"message": "Logged out successfully"}