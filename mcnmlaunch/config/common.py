#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Immutable basic settings.
"""
import logging

from mcnmlaunch.config import op, ROOTDIR
from os import environ

SECRET_KEY = 'srU7190rKKiQa8+ZL5sVTEcNAPiSmpv3'

#----------------------WTFORMS-------------------------------------------
CSRF_ENABLED = True
CSRF_SESSION_KEY = '9G8dfmxIPEtl5shwS0aLGb5Z66MihXSp'

#-----------------------MANDRILL-----------------------------------------
FROM_EMAIL = 'dispatch@myconomy.ru'
FROM_NAME  = u'Myconomy'
EMAIL_ARCHIVE = 'mail-archive@myconomy.ru'

#----------------------- FLASK-S3 -----------------------------------------
AWS_ACCESS_KEY_ID       = 'AKIAIIWX7Y7P3RJBF3OQ'
AWS_SECRET_ACCESS_KEY   = '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'
S3_BUCKET_NAME          = 'mcnmlaunchstatic'
USE_S3                  = False
USE_S3_DEBUG            = False

#-----------------------SENTRY-----------------------------------------
SENTRY_DSN = 'https://2a258a0d834c49848c5c2edc7728a1e8:e67dc678fe5e45d4b4d343731ae8d463@app.getsentry.com/2370'
SENTRY_USER_ATTRS = ['id', 'username', 'first_name', 'last_name', 'email']


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', datefmt='%d.%m %H:%M:%S')
logging.info("Core settings loaded.")

