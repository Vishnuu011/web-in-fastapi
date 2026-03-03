from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient
from config.Env import ENVConfig


client = AsyncIOMotorClient(ENVConfig.MONGO_URI)
db = client[ENVConfig.MONGO_DB]

#User collecton

user_collection = db["users"]