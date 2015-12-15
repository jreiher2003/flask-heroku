import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\x82\x8aJ\xect\xd1\x14\xcc\xf1 \xbdC\xe5\x97h\xe8\xa1\xc5\t\x12\xe3\xeb\x83\x16'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False