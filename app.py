#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname((os.path.realpath(__file__))), 'mcnmlaunch'))

from mcnmlaunch import create_app

app = create_app()

if __name__ == '__main__':

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)