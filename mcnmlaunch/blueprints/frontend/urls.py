#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mcnmlaunch.views.base import ShowView
from mcnmlaunch.blueprints.frontend.view import StoreEmailView

def get_urls():
    return (
        ('',  ShowView.as_view('index', template_name='index.html')),
        ('store', StoreEmailView.as_view('store')),

    )