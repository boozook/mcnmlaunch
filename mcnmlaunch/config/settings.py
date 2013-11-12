#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Application settings
"""
import sys
import os
import importlib

from mcnmlaunch.config.common import *

# Load appropriate settings.
environ = os.environ.get('MCNMLAUNCH_SETTINGS')

# Set environment specific settings.
if environ:
    _this_module = sys.modules[__name__]
    try:
        _m = importlib.import_module('mcnmlaunch.config.%s' % environ)
    except ImportError, ex:
        print ex
    else:
        for _k in dir(_m):
            setattr(_this_module, _k, getattr(_m, _k))

# Production is the default environment.
else:
    try:
        from production import *
    except ImportError, ex:
        pass