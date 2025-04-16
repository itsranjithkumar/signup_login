# test_mongo.py
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv("MONGO_URL"))

try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
