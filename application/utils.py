# -*- coding: utf-8 -*-
"""
    application.utils
    ~~~~~~~~~~~~~~~~~

    Craic utilities.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from flask import current_app
from socket import gaierror, gethostbyname


def is_local(environment):
    """Determine if the current request is local.

    :param environment: The current WSGI environment.
    """
    ret_val = False
    server_name = environment["SERVER_NAME"]

    try:
        host = gethostbyname(server_name)

        if host in ("127.0.0.1", "::1"):
            ret_val = True
    except gaierror, e:
        current_app.logger.error(e)

    return ret_val
