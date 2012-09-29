#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mcnmlaunch.views.base import ShowView
from mcnmlaunch.blueprints.frontend.view import StoreEmailView, ShowSplitView

def get_urls():
    return (
        ('',  ShowSplitView.as_view('index', template_name='index_a.html')),
        ('a',  ShowView.as_view('index_a', template_name='index_a.html')),
        ('b',  ShowView.as_view('index_b', template_name='index_b.html')),
        ('c',  ShowView.as_view('index_c', template_name='index_c.html')),
        ('store', StoreEmailView.as_view('store')),

    )