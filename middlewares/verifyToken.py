from fastapi import Request, HTTPException
import jwt

from config.Env import ENVConfig 



def verifyToken(req: Request):

    authraization = req.headers.get(
            "Authorization",""
        )
    if not authraization or not authraization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Please login first"
        )
    token = authraization.split(" ")[1]
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Please login first"
        )

    try:

        payload = jwt.decode(
            token,
            ENVConfig.JWT_AUTH_SECRET_KEY,
            algorithms=[ENVConfig.ALGORITHM]
        )
        return payload["user_id"]
        
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail=f"Unauthorized: {str(e)}"
        )