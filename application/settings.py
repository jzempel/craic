# -*- coding: utf-8 -*-
"""
    application.settings
    ~~~~~~~~~~~~~~~~~~~~

    Craic application settings.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from os.path import abspath, dirname, join

STYLUS_EXTRA_ARGS = ["--include",
        join(abspath(dirname(__file__)), "../blueprints/web/static/_styl/")]
STYLUS_PLUGINS = ["nib"]
UGLIFYJS_EXTRA_ARGS = ["--no-copyright"]
VERSION_JQUERY = "1.8.2"
VERSION_MODERNIZR = "2.6.2"
VERSION_NORMALIZE = "2.0.1"

try:
    from .settings_local import *  # NOQA
except ImportError:
    pass
