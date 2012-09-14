# -*- coding: utf-8 -*-
from __future__ import absolute_import

from werkzeug.datastructures import MultiDict
from flask import flash
from flask.views import View

from flask import redirect, request, render_template

class ShowView(View):
    methods = ['GET']

    def __init__(self, template_name):
        self.template_name = template_name

    def render_template(self, **context):
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        context = {}
        return self.render_template(**context)
