#!/usr/bin/env python
#coding=utf-8

import uuid
import pprint
from random import randint
from datetime import datetime


from flask import Flask, current_app
from flask.ext.script import Server, Shell, Manager, Command, prompt_bool

from mcnmlaunch import create_app

manager = Manager(create_app)

manager.add_command("runserver", Server('127.0.0.1',port=12345))

@manager.shell
def make_shell_context():
    return dict(app=current_app,
                db=db)

@manager.command
def dumpconfig():
    "Dumps config"
    pprint.pprint(current_app.config)

manager.add_option("-c", "--config",
                   dest="config",
                   help="config file",
                   required=False)

if __name__ == "__main__":
    manager.run()
