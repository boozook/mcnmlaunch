#!/usr/bin/env python
# -*- coding: utf-8 -*-

" Production settings must be here. "

from .core import *
from os import path as op, environ

SECRET_KEY = 'srU7190rKKiQa8+ZL5sVTEcNAPiSmpv3'

# Mail (gmail config)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'klinkin@gmail.com'
MAIL_PASSWORD = '2RzWsEgCBrzA'
DEFAULT_MAIL_SENDER = 'Admin < %s >' % MAIL_USERNAME

ADMINS = frozenset([MAIL_USERNAME])
COLLECT_STATIC_ROOT = op.join(op.dirname(ROOTDIR), 'static')
