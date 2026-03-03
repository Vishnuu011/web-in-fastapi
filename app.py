from fastapi import FastAPI

#Fastapi instance
app=FastAPI()

app.get("/", tags=['health'])
def healthRoute():
    return {
        "msg":"Server is working Correctly"
    }


