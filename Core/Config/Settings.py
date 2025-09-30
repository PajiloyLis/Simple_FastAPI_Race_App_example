import os
from dotenv import load_dotenv

from Core.Common.Singleton import SingletonMeta

load_dotenv()

class Settings(metaclass=SingletonMeta):
    database_url = None
    host = None
    port = None
    def __init__(self):
        self.load_settings()

    async def load_settings(self):
        database_url = os.getenv("DB_URL")
        host = os.getenv("HOST")
        port = os.getenv("PORT")
