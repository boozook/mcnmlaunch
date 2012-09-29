# -*- coding: utf-8 -*-
from __future__ import absolute_import
from random import randint

from flask.views import View
from flask import redirect, request, render_template, jsonify, url_for
from mcnmlaunch.extensions import valid_email_address, mailchimp_api

class ShowSplitView(View):
    methods = ['GET']

    def __init__(self, template_name):
        self.template_name = template_name

    def render_template(self, **context):
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        variant = randint(1, 3)

        if variant == 1:
	        context = {}
	        return self.render_template(**context)
        elif variant == 2:
            return redirect(url_for('frontend.index_b'))
        elif variant == 3:
            return redirect(url_for('frontend.index_c'))
        else:
            context = {}
            return self.render_template(**context)

class StoreEmailView(View):
    methods = ['POST']

    def dispatch_request(self):
        if ('email' not in request.form) or (str(request.form['email'].encode('utf-8')) == str('')):
            return jsonify({'success':False, 'msg':u'Заполните поле e-mail адреса.'})

        if not valid_email_address(str(request.form['email'].encode('utf-8'))):
            return jsonify({'success':False, 'msg':u'E-mail адрес указан неверно.'})

        if mailchimp_api.listSubscribe(id='a972b72a63', email_address=str(request.form['email'].encode('utf-8')), double_optin=False, send_welcome=False):
            return jsonify({'success':True, 'msg':u'Спасибо за доверие! Мы не подведем :)'})
        else:
            return jsonify({'error':True, 'msg':u'Что-то пошло не так, как мы задумывали(: Но мы скоро это исправим!'})
        return jsonify({'ok'})
