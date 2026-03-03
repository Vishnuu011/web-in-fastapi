from fastapi import APIRouter
from typing import Any
from controllers.authController import registerController
from models.authModel import User as UserModel
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

    return await registerController(data.dict())