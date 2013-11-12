#!/usr/bin/env python
# -*- coding: utf-8 -*-
from injector import Module, inject, singleton
from flask import render_template, request, url_for, jsonify
from flask.ext.classy import FlaskView, route
from email_validation import valid_email_address
from mailchimp import Mailchimp

from mcnmlaunch.di import inj


class IndexView(FlaskView):

    @route('', methods=('GET',))
    def promo(self):
        return render_template("index.html")

    @route('save', methods=('POST',))
    def save(self):
        r = inj.get(Mailchimp).lists.subscribe(id='ea27cc63ba', 
                                               email=dict(email=str(request.form['email'].encode('utf-8'))),
                                               merge_vars=dict(FNAME=str(request.form['name'].encode('utf-8')),
                                                               COMPANY=str(request.form['company'].encode('utf-8')),
                                                               PHONE=str(request.form['phone'].encode('utf-8'))
                                                              ),
                                               double_optin=False,
                                               send_welcome=False)

        if r['euid']:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})