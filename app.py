from fastapi import FastAPI
from routers.authRoute import router as AuthRouter
from fastapi.middleware.cors import CORSMiddleware



#Fastapi instance
app=FastAPI()



#Routers
app.include_router(AuthRouter)

app.get("/", tags=['health'])
def healthRoute():
    return {
        "msg":"Server is working Correctly"
    }


