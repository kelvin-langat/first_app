import os

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USERNAME = os.getenv("DB_USERNAME", "user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")