#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Development settings.
"""
import logging
from mcnmlaunch.config import ROOTDIR
from os import path as op, environ

DEBUG = True
TRAP_HTTP_EXCEPTIONS = True
TRAP_BAD_REQUEST_ERRORS = True
SQLALCHEMY_ECHO = False

logging.info("Develop settings loaded.")