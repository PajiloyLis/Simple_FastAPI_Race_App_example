import os
from dotenv import load_dotenv

from Core.Common.Singleton import SingletonMeta

load_dotenv()

class Settings(metaclass=SingletonMeta):
    def __init__(self):
        self.database_url = None
        self.host = None
        self.port = None
        self.load_settings()

    def load_settings(self):
        self.database_url = str(os.getenv("DB_URL"))
        self.host = str(os.getenv("HOST"))
        self.port = int(os.getenv("PORT"))
