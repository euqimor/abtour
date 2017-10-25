from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

with open('secret.txt') as f:
    SECRET_KEY = f.read().strip()

try:
    from .local import *
except ImportError:
    pass
