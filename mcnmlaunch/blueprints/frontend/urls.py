#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.wtf import TextField, Required, Email

from mcnmlaunch.views.base import ShowView

def get_urls():
    return (
        ('',  ShowView.as_view('index', template_name='index.html')),

    )