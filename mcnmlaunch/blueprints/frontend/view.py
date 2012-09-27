# -*- coding: utf-8 -*-
from __future__ import absolute_import

from werkzeug.datastructures import MultiDict
from flask.views import View
from flask import redirect, request, render_template, jsonify
from mcnmlaunch.extensions import valid_email_address, mailchimp_api

class StoreEmailView(View):
    methods = ['POST']

    def dispatch_request(self):
        if ('email' not in request.form) or (str(request.form['email']) == str('')):
            return jsonify({'success':False, 'msg':u'Заполните поле e-mail адреса.'})

        if not valid_email_address(str(request.form['email'])):
            return jsonify({'success':False, 'msg':u'E-mail адрес указан неверно.'})

        if mailchimp_api.listSubscribe(id='a972b72a63', email_address=str(request.form['email']), double_optin=False, send_welcome=False):
            return jsonify({'success':True, 'msg':u'Спасибо за доверие! Мы не подведем :)'})
        else:
            return jsonify({'error':True, 'msg':u'Что-то пошло не так, как мы задумывали(: Но мы скоро это исправим!'})
        return jsonify({'ok'})
