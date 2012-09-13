# -*- coding: utf-8 -*-
from __future__ import absolute_import

from flask.views import View

from flask import redirect, request, render_template

class ShowView(View):
    methods = ['GET']

    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title
    
    def render_template(self, **context):
        return render_template(self.template_name, **context)
    
    def dispatch_request(self):
        context = {'title': self.title}
        return self.render_template(**context)

class FormView(View):
    methods = ['GET', 'POST']

    def render_template(self, **context):
        return render_template(self.template_name, **context)

    def redirect(self, url):
        return redirect(url)

    def dispatch_request(self):
        form = self.get_form()
        if request.method == 'POST':
            return self.form_handler(form=form)
        else:
            context = {'form': form, 'title': self.get_title()}
            return self.render_template(**context)
