from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class DatabaseConnection:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MongoClient(os.getenv('MONGODB_URI'))
        return cls._instance

    @classmethod
    def get_database(cls):
        client = cls.get_instance()
        return client[os.getenv('MONGODB_DB_NAME')]