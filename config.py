import os

SECRET_KEY = "something very secret"

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True

AD_HOST = 'ad.bboxx.co.uk'
AD_PORT = 3268
