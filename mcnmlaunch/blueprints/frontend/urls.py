#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mcnmlaunch.views.base import ShowView

def get_urls():
    return (
        ('',  ShowView.as_view('index', template_name='index.html', title='Myconomy Dashboard')),
    )