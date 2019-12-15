# import os

# # You need to replace the next values with the appropriate values for your configuration

# basedir = os.path.abspath(os.path.dirname(__file__))
# SQLALCHEMY_ECHO = False
# SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"


import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI ="sqlite:///app.db" # os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}