import os


# default config
class BaseConfig(object):
    """ common configs between local and production """
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = '\x82\x8aJ\xect\xd1\x14\xcc\xf1 \xbdC\xe5\x97h\xe8\xa1\xc5\t\x12\xe3\xeb\x83\x16'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # print SQLALCHEMY_DATABASE_URI


class DevelopmentConfig(BaseConfig):
    """ local environment settings """
    DEBUG = True


class ProductionConfig(BaseConfig):
    """ heroku production settings for a live environment """
    DEBUG = False