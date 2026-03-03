from fastapi import APIRouter, HTTPException
from typing import Any
from controllers.authController import registerController, loginController
from models.authModel import User as UserModel
from models.authModel import LoginModel 
from config.db import user_collection


router=APIRouter(
    prefix="/api/v1/auth",
    tags=['auth']
)

""""
GET -> collection the data {JSON, HTML/text}
POST -> create a new data
PUT -> update the data
DELETE -> delete the data
"""""

#register route

@router.post("/register")
async def registerView(data: UserModel):

    try:
        return await registerController(data)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during registration: {str(e)}"
        )

@router.post("/login")
async def loginView(data: LoginModel):
    try:
        return await loginController(data)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred during login: {str(e)}"
        )