from application.util import generate

class Config(object):
    SECRET_KEY = generate(50)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'xclow3n'
    MYSQL_PASSWORD = 'xCl0w3n1337!!'
    MYSQL_DB = 'web_htbank'
    PHP_HOST = '127.0.0.1:80'

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True