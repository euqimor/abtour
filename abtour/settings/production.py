from __future__ import absolute_import, unicode_literals
from os import environ

from .base import *

DEBUG = False

SECRET_KEY = environ['django_prod_secret']

try:
    from .local import *
except ImportError:
    pass
