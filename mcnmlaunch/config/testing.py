#!/usr/bin/env python
# -*- coding: utf-8 -*-
" Settings for running tests. "

import logging
from mcnmlaunch.config import ROOTDIR
from os import path as op

TESTING = True
DEBUG = False

# TRAP_HTTP_EXCEPTIONS = True
# TRAP_BAD_REQUEST_ERRORS = True

logging.info("Test settings loaded.")