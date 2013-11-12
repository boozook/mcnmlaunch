#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from flask import request, render_template, jsonify

def generic_error_handler(error):

    if error.description:
        # чистим описание от тегов
        p = re.compile(r'<.*?>')
        error.description = p.sub('', error.description)

    result = {
               "meta": {
                   "code": error.code
               },
               "response": {
                   "error": {
                       "description": error.description,
                       "name": error.name,
                       "page_title": "Error %d %s" % (error.code, error.name),
                   }
               }
             }

    try:
        return render_template("errors/%d.html" % error.code, **result), error.code
    except:
        return render_template("errors/generic.html", **result), error.code
