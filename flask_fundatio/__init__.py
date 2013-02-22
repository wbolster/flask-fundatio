"""
Flask-Fundatio extension module
"""

from __future__ import absolute_import

from flask import Blueprint


class Fundatio(object):
    """Flask-Fundatio extension class"""

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
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
