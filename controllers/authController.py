from services.authService import loginService, registerService
from models.authModel import User as UserModel
from models.authModel import LoginModel


async def registerController(data: UserModel):
    return await registerService(data)

async def loginController(data: LoginModel):
    return await loginService(data)