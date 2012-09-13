#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path as op

from flask import Flask, render_template, request, jsonify

from mcnmlaunch.blueprints import frontend
from mcnmlaunch.config import production, test

__all__ = ["create_app"]

DEFAULT_APP_NAME = "mcnmlaunch"

DEFAULT_BLUEPRINTS = (
     (frontend.bp, '/'),

)

def create_app(config=None, app_name=None, blueprints=None):

    if app_name is None:
        app_name = DEFAULT_APP_NAME

    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(__name__)
    configure_app(app, config)

    configure_errorhandlers(app)

    with app.test_request_context():
        from mcnmlaunch.extensions import configure_extensions
        configure_extensions(app)

    configure_context_processors(app)
    configure_blueprints(app, blueprints)

    print repr(app.url_map)
    app.logger.info(repr(app.url_map))

    return app

def configure_app(app, config):
    app.config.from_object(config or production)
#    app.config.from_object(config or test)

def configure_blueprints(app, blueprints):
    for blueprint, url_prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=url_prefix)

def configure_context_processors(app):

    @app.context_processor
    def config():
        return dict(config=app.config)

def configure_errorhandlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        if request.is_xhr:
            return jsonify(error='Sorry, page not found')
        return render_template("errors/404.html", error=error)

    @app.errorhandler(403)
    def forbidden(error):
        if request.is_xhr:
            return jsonify(error='Sorry, not allowed')
        return render_template("errors/403.html", error=error)

    @app.errorhandler(500)
    def server_error(error):
        if request.is_xhr:
            return jsonify(error='Sorry, an error has occurred')
        return render_template("errors/500.html", error=error)

    @app.errorhandler(401)
    def unauthorized(error):
        if request.is_xhr:
            return jsonify(error="Login required")
        return render_template("errors/401.html", error=error)