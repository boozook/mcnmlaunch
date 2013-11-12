#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from injector import Module, inject, singleton

from flask.ext.cache import Cache
from raven.contrib.flask import Sentry
from dealer.contrib.flask import Dealer
from mailchimp import Mailchimp


@inject(app=Flask)
class DealerModule(Module):

    def configure(self, binder):

        dealer = Dealer(app=self.app)
        binder.bind(Dealer, to=dealer, scope=singleton)


@inject(app=Flask)
class SentryModule(Module):

    def configure(self, binder):

        sentry = Sentry(app=self.app)
        binder.bind(Sentry, to=sentry, scope=singleton)


@inject(app=Flask)
class MailChimpModule(Module):

    def configure(self, binder):

        mc = Mailchimp(apikey='d6efe663097ecd16a1b17c2e4283a5d8-us5')
        binder.bind(Mailchimp, to=mc, scope=singleton)


@inject(app=Flask)
class CacheModule(Module):

    def configure(self, binder):

        cache = Cache(app=self.app)
        binder.bind(Cache, to=cache, scope=singleton)

