#!/usr/bin/env python
# -*- coding: utf-8 -*-

from raven.contrib.flask import Sentry
from flask.ext.cache import Cache
from flask.ext.debugtoolbar import DebugToolbarExtension
from mailsnake import MailSnake
from email_validation import valid_email_address

__all__ = ['cache', 'mandrill_api', 'mailchimp_api']

sentry = Sentry()
cache = Cache()

mandrill_api = MailSnake('5a4fa284-08ff-47fe-abba-d87cf89ed824', api='mandrill')

mailchimp_api = MailSnake('d6efe663097ecd16a1b17c2e4283a5d8-us5', api='api')


def configure_extensions(app):
    sentry.init_app(app)
    cache.init_app(app)
