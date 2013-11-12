#!/usr/bin/env python
# -*- coding: utf-8 -*-

" Settings for running tests. "

from .production import *


TESTING = True

CSRF_ENABLED = False
CACHE_TYPE = 'simple'