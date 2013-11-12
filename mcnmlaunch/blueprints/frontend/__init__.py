#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from .views import IndexView


bp = Blueprint('frontend', __name__)

IndexView.register(bp, route_base='/')
