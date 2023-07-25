from .base import *

import os

DEBUG = False

ALLOWED_HOSTS = [os.environ.get("ALLOWED_HOSTS")]

try:
    from .local import *
except ImportError:
    pass
