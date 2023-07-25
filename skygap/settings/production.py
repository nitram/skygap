from .base import *
from decouple import config

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET')

ALLOWED_HOSTS = [config('SERVER')]

try:
    from .local import *
except ImportError:
    pass
