# -*- coding: utf-8 -*-
"""
    web.views.commons
    ~~~~~~~~~~~~~~~~~

    View commons.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from flask import g, render_template, request
from flask.ext.babel import gettext


def about():
    """About page.
    """
    g.title = gettext("About")
    template = "web/commons/about.html"

    if request.is_pjax:
        ret_val = render_template(template)
    else:
        ret_val = render_template("web/base.html", template=template)

    return ret_val


def css():
    """CSS documentation page.
    """
    g.title = gettext("CSS")
    template = "web/commons/css.html"

    if request.is_pjax:
        ret_val = render_template(template)
    else:
        ret_val = render_template("web/base.html", template=template)

    return ret_val


def landing():
    """Landing page.
    """
    return render_template("web/base.html")
