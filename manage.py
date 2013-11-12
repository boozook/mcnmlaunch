#!/usr/bin/env python
#coding=utf-8

from flask import url_for
from flask.ext.script import Server, Shell, Manager

from mcnmlaunch import create_app

app = create_app()
manager = Manager(app)
manager.add_command("runserver", Server('127.0.0.1',port=12345))

@manager.command
def routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line

def _make_context():
    return dict(app=app)

manager.add_command("shell", Shell(make_context=_make_context))
manager.run()
