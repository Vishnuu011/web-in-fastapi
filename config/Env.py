from dotenv import load_dotenv
import os       

load_dotenv()


class ENVConfig:

    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DB: str = os.getenv("MONGO_DB")