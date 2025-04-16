from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserResponse
from app.database import user_collection
from passlib.hash import bcrypt
from datetime import datetime

router = APIRouter()

# Register route
@router.post("/auth/register", response_model=UserResponse)
def register_user(user: UserCreate):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    hashed_pwd = bcrypt.hash(user.password)
    user_dict = {
        "name": user.name,
        "email": user.email,
        "hashed_password": hashed_pwd,
        "created_at": datetime.utcnow()
    }
    user_collection.insert_one(user_dict)
    return {"name": user.name, "email": user.email}
