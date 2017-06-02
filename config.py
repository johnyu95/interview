import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # Flask-SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # remove once this becomes the default


    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    # DEBUG = True
    # SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
    #                           'postgresql://localhost:5432/womens_activism_dev')
    pass

   


class TestingConfig(Config):
    # TESTING = True
    # SQLALCHEMY_DATABASE_URI = (os.environ.get('TEST_DATABASE_URL') or
    #                           'postgresql://localhost:5432/womens_activism_test')
    pass


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
    #                           'postgresql://localhost:5432/womens_activism_nyc_v2')
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
