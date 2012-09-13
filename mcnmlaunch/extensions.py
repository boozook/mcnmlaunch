#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raven.contrib.flask import Sentry
from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension

__all__ = ['cache']

sentry = Sentry()
cache = Cache()

def configure_extensions(app):
    sentry.init_app(app)
    cache.init_app(app)