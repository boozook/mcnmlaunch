#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raven.contrib.flask import Sentry
from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension
from mailsnake import MailSnake

__all__ = ['cache', 'mandrill_api']

sentry = Sentry()
cache = Cache()

mandrill_api = MailSnake('5a4fa284-08ff-47fe-abba-d87cf89ed824', api='mandrill')

def configure_extensions(app):
    sentry.init_app(app)
    cache.init_app(app)
