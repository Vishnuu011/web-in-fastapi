from fastapi import HTTPException

from services.authService import loginService, registerService, profileService
from models.authModel import User as UserModel
from models.authModel import LoginModel


async def registerController(data: UserModel):
    
    try:
        return await registerService(data)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during registrationController: {str(e)}"
        )

async def loginController(data: LoginModel):
    try:
        return await loginService(data)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during loginController: {str(e)}"
        )
    

async def profileController(user_Id: str):
    
    try:
        return await profileService(user_Id)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during profileController: {str(e)}"
        )

