# -*- coding: utf-8 -*-
"""
    web
    ~~~

    Web blueprint.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from .views import about, css, landing
from application.extensions import environment
from flask import Blueprint
from flask.ext.assets import Bundle

blueprint = Blueprint(__name__, __name__, static_folder="static",
        static_url_path='', template_folder="templates")
blueprint.add_url_rule('/',
        view_func=landing)
blueprint.add_url_rule("/css",
        view_func=css)
blueprint.add_url_rule("/about",
        view_func=about)
bundle = Bundle("css/normalize.css", "web/_styl/commons.styl",
        "web/_styl/responsive.styl", filters="stylus")
environment.register("css", bundle)
