import os

class Config:
    JWT_SECRET_KEY = os.urandom(69).hex()
    DEBUG = False
