from application.util.general import generate

class Config(object):
	SECRET_KEY = generate(50)
	SESSION_TYPE = "filesystem"

class ProductionConfig(Config):
	pass


class DevelopmentConfig(Config):
	DEBUG = False


class TestingConfig(Config):
	TESTING = False