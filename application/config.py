

class Config(object):
    DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5444/flask'

class ProductionConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5444/flask'

class DevelopmentConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5444/flask'
    HOST_RABBIT = '127.0.0.1'

class TestingConfig(Config):
    TESTING = True