from .base import *
from decouple import config

import os

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET')

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]

try:
    from .local import *
except ImportError:
    pass
