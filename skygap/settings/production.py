from .base import *
from decouple import config

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = [config('SERVER')]

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN


try:
    from .local import *
except ImportError:
    pass
