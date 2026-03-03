from config.Env import ENVConfig
from config.db import user_collection


async def registerService(data):

    doc = await user_collection.insert_one(
        data
    )

    print(doc)
    return {
        "message": "User registered successfully",
        "user_id": str(doc.inserted_id)  
    }