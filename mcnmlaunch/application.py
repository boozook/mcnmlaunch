#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.injector import init_app, post_init_app

from mcnmlaunch.config import settings
from mcnmlaunch.errors import generic_error_handler

from mcnmlaunch.di import inj

from mcnmlaunch import extensions as exts

__all__ = ["create_app"]

def create_app():

    app = Flask("mcnmlaunch")

    configure_app(app)
    configure_errorhandlers(app)

    modules = [exts.DealerModule, exts.MailChimpModule, exts.SentryModule, exts.CacheModule]

    injector = init_app(app=app, injector=inj, modules=modules)


    load_blueprints(app)

    post_init_app(app, injector)
    print repr(app.url_map)

    return app

def configure_app(app):
    app.config.from_object(settings)

def load_blueprints(app):
    from mcnmlaunch.blueprints import frontend
    blueprints = (
                   (frontend.bp, ''),
                 )

    for blueprint, url_prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=url_prefix)

def configure_errorhandlers(app):

    for error in range(400, 420) + range(500,506):
        app.error_handler_spec[None][error] = generic_error_handler


