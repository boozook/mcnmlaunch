#!/usr/bin/env python
# -*- coding: utf-8 -*-

" Core configuration settings. "

from mcnmlaunch.config import op, ROOTDIR

# WTForms
CSRF_ENABLED = True
CSRF_SESSION_KEY = '9G8dfmxIPEtl5shwS0aLGb5Z66MihXSp'


#----------------------MEDIA--------------------------------------------
STATIC_URL = 'https://s3-eu-west-1.amazonaws.com/mcnmlaunch/static'
#STATIC_URL = 'static'

#-----------------------SENTRY-----------------------------------------
SENTRY_DSN = 'https://2a258a0d834c49848c5c2edc7728a1e8:e67dc678fe5e45d4b4d343731ae8d463@app.getsentry.com/2370'
