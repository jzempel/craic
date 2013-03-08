# -*- coding: utf-8 -*-
"""
    application
    ~~~~~~~~~~~

    Craic application.

    :copyright: 2012 by Jonathan Zempel.
    :license: BSD, see LICENSE for more details.
"""

from .extensions import babel, environment
from .utils import is_local
from flask import Flask, g, request, Request as BaseRequest
from flask.ext.babel import gettext
from werkzeug.useragents import UserAgent
from werkzeug.wsgi import SharedDataMiddleware
import os
import settings


class Request(BaseRequest):
    """Custom request class.
    """

    @property
    def is_pjax(self):
        """Determine if the current request was sent via PJAX.
        """
        return "HTTP_X_PJAX" in self.environ


def create(static_url_path='', configuration=None, settings=settings,
           environment_variable="CRAIC_SETTINGS", blueprints=[]):
    """Create the Craic application.

    :param static_url_path: Default ``''``. Specify the URL path for static
        files.
    :param configuration: Default `None`. Python configuration file name.
    :param settings: Default :mod:`settings`. Default configuration settings -
        used only if `configuration` is not provided.
    :param environment_variable: Default ``'CRAIC_SETTINGS'``. The name of the
        environment variable that points to a configuration file - overrides
        any existing configuration setting.
    :param blueprints: Default `[]`. A list of application blueprints.
    """
    ret_val = Flask(__name__, static_url_path=static_url_path)
    ret_val.request_class = Request

    if configuration:
        ret_val.config.from_pyfile(configuration)
    else:
        ret_val.config.from_object(settings)

    ret_val.config.from_envvar(environment_variable, silent=True)
    init_extensions(ret_val)
    init_blueprints(ret_val, *blueprints)
    init_middleware(ret_val)

    @ret_val.before_request
    def before_request():
        g.is_local = is_local(request.environ)
        g.user_agent = UserAgent(request.environ)

    @ret_val.context_processor
    def context_processor():
        if hasattr(g, "title"):
            title = gettext("Craic / %(title)s", title=g.title)
        else:
            title = gettext("Craic.")

        return dict(title=title)

    return ret_val


def init_blueprints(application, *blueprints):
    """Initialize application blueprints.

    :param application: The application to initialize blueprints for.
    :param *blueprints: The blueprints to initialize.
    """
    application.url_map.strict_slashes = False

    for blueprint in blueprints:
        application.register_blueprint(blueprint)


def init_extensions(application):
    """Initialize application extensions.

    :param application: The application to initialize extensions for.
    """
    babel.init_app(application)
    environment.init_app(application)


def init_middleware(application):
    """Initialize application WSGI middleware.

    :param application: The application to initialize middleware for.
    """
    exports = {}

    for blueprint in application.blueprints.itervalues():
        if blueprint.has_static_folder:
            url_path = blueprint.static_url_path or '/'

            if blueprint.url_prefix:
                url_path = "{0}{1}".format(blueprint.url_prefix, url_path)

            exports[url_path] = blueprint.static_folder

    for name in os.listdir(application.static_folder):
        if not name.startswith('.'):
            path = os.path.join(application.static_folder, name)

            if os.path.isdir(path):
                exports["/{0}".format(name)] = path

    application.wsgi_app = SharedDataMiddleware(application.wsgi_app, exports,
            cache_timeout=31536000)
