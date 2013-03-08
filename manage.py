# -*- coding: utf-8 -*-
"""
    manage
    ~~~~~~

    Craic application manager.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

import os
import sys

directory = os.path.dirname(os.path.abspath(__file__))
path = "{0}/blueprints".format(directory)

if path not in sys.path:
    sys.path.append(path)

from application import create
from flask.ext.script import Manager
from web import blueprint as web


def create_app():
    """Create the application.
    """
    blueprints = [web]

    return create(blueprints=blueprints)


manager = Manager(create_app)

if __name__ == "__main__":
    manager.run()
