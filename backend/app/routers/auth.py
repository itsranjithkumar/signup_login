from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserCreate, UserResponse, UserLogin
from app.database import user_collection
from passlib.hash import bcrypt
from datetime import datetime

router = APIRouter()

# Register route
@router.post("/auth/register", response_model=UserResponse)
def register_user(user: UserCreate):
    # Check if email already exists
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    
    # Hash the password before storing
    hashed_pwd = bcrypt.hash(user.password)
    
    # Store the user data in MongoDB
    user_dict = {
        "name": user.name,
        "email": user.email,
        "hashed_password": hashed_pwd,
        "created_at": datetime.utcnow()
    }
    
    # Insert the new user document into the database
    user_collection.insert_one(user_dict)
    
    # Return the user data, excluding the password (mapped to UserResponse schema)
    return UserResponse(
        name=user.name,
        email=user.email,
        created_at=user_dict["created_at"]
    )

# Login route
@router.post("/auth/login", response_model=UserResponse)
def login_user(user: UserLogin):
    # Check if the email exists in the database
    existing_user = user_collection.find_one({"email": user.email})
    
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Verify the password using bcrypt
    if not bcrypt.verify(user.password, existing_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Return the user's data (mapped to UserResponse schema)
    return UserResponse(
        name=existing_user["name"],
        email=existing_user["email"],
        created_at=existing_user["created_at"]
    )
