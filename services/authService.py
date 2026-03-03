from config.Env import ENVConfig
from config.db import user_collection
from fastapi.exceptions import HTTPException
from models.authModel import User as UserModel
from models.authModel import LoginModel
import bcrypt


async def registerService(data:UserModel):

    try:
        check_user = await user_collection.find_one(
            {
                "email":data.email.lower()
            }
        )
        if check_user:
            raise HTTPException(
                status_code=400,
                detail="User with this email already exists"
            )

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(
            data.password.encode(),
            salt
        ).decode()

        user_data = data.dict()
        user_data["password"] = hashed_password
        
        doc = await user_collection.insert_one(
           user_data
        )

        return {
           "message": "User registered successfully",
           "token": "" 
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during registration: {str(e)}"
        )
    
async def loginService(data:LoginModel):

    try:
        check_user = await user_collection.find_one(
            {
                "email":data.email.lower()
            }
        )
        if not check_user:
            raise HTTPException(
                status_code=404,
                detail="User not Exist"
            )   
        
        is_match = bcrypt.checkpw(
            data.password.encode(),
            check_user['password'].encode()
        )
        if not is_match:
            raise HTTPException(
                status_code=400,
                detail="Invalid credentials"
            )
        
        token = ""

        return {
            "message": "Login successful",
            "token": token
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during login: {str(e)}"
        )