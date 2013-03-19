"""
Flask-Fundatio extension module
"""

from __future__ import absolute_import

from flask import Blueprint

JAVASCRIPT_LIBRARIES = ('auto', 'jquery', 'zepto')
DEFAULT_JAVASCRIPT_LIBARY = 'jquery'


class Fundatio(object):
    """Flask-Fundatio extension class"""

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialise the `app` for use with :py:class:`~Fundatio`.

        This method is automatically invoked if an `app` instance is
        passed to the :py:class:`~Fundatio` constructor.

        Fundatio uses the following configuration variables:

        * ``FUNDATIO_JAVASCRIPT_LIBRARY``
        """

        javascript_library = app.config.setdefault(
            'FUNDATIO_JAVASCRIPT_LIBRARY', DEFAULT_JAVASCRIPT_LIBARY)
        if not javascript_library in JAVASCRIPT_LIBRARIES:
            raise ValueError(
                "Invalid 'FUNDATIO_JAVASCRIPT_LIBRARY' value in config; "
                "must be one of %r, but found %r"
                % (JAVASCRIPT_LIBRARIES, javascript_library))

        blueprint = Blueprint(
            'fundatio',
            __name__,
            static_folder='static',
            # XXX: specify explicit static url path to work around
            # https://github.com/mitsuhiko/flask/issues/348
            static_url_path='%s/foundation' % app.static_url_path,
            template_folder='templates',
        )
        app.register_blueprint(blueprint)
