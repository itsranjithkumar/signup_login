from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth  # Make sure this import is correct

app = FastAPI()

origins = [
    "http://localhost:3000",  # Update with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)  # Include the auth router here
