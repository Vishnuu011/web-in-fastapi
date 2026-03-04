from dotenv import load_dotenv
import os       

load_dotenv()


class ENVConfig:

    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DB: str = os.getenv("MONGO_DB")
    JWT_AUTH_SECRET_KEY: str = os.getenv("JWT_AUTH_SECRET_KEY","##$%$#@@##$$%&*)_(*&^)")
    ALGORITHM: str = "HS256"