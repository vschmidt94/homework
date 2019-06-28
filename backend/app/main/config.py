import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'the_very_secret_key')
    DEBUG = False

# RVW: SQLLite is a pain in the a$$ for most migrations, but has a good role here.
#      Suggest adding some manager commands to wipe the DBs and re-init. It's
#      a hassle to have to do that more than once as DB evolves.
# RVW: Explicit is better than implicit. Suggest both dev config, testing config, and prod config
#      explicitly call out same settings so differences between the configs jump out.
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_api_dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_api_test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_api_prod.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


config_by_name = {'dev': DevelopmentConfig,
                  'test': TestingConfig,
                  'prod': ProductionConfig}

key = Config.SECRET_KEY
