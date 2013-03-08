# -*- coding: utf-8 -*-
"""
    application.extensions
    ~~~~~~~~~~~~~~~~~~~~~~

    Craic application extensions.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from flask.ext.assets import Environment
from flask.ext.babel import Babel

babel = Babel()
environment = Environment()
