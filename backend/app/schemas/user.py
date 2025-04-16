from pydantic import BaseModel
from datetime import datetime

# User creation schema
class UserCreate(BaseModel):
    name: str
    email: str
    password: str  # Plaintext password, will be hashed before storing

# User response schema (output for user-related data)
class UserResponse(BaseModel):
    name: str
    email: str
    created_at: datetime

    class Config:
        orm_mode = True  # To ensure that MongoDB _id is converted to a string
        # Add this if you want to ensure that datetime is serialized as an ISO string
        json_encoders = {
            datetime: lambda v: v.isoformat() if isinstance(v, datetime) else v
        }

# User login schema (input for login credentials)
class UserLogin(BaseModel):
    email: str
    password: str  # Plaintext password provided during login
