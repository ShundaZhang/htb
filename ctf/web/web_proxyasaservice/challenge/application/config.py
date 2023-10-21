import os

class Config(object):
    SECRET_KEY = os.urandom(69).hex()

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True