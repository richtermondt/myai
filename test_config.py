import os


class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = os.getenv('SECRET_KEY', 'test_secret_key')
