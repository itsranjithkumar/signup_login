import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URL"))
db = client["auth_db"]  # The database name

# MongoDB collection for users
user_collection = db["users"]
