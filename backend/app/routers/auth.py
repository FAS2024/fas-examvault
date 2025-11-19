from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserCreate
from app.core.security import hash_password

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    hashed_pw = hash_password(user.password)
    # Save to DB logic goes here
    return {"msg": f"User {user.username} registered successfully."}

@router.post("/login")
async def login():
    return {"msg": "Login endpoint"}
