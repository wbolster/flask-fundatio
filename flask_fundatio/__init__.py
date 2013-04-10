"""
Flask-Fundatio extension module
"""

from __future__ import absolute_import

from flask import Blueprint

try:
    import wtforms
    wtforms  # silence flake8
    has_wtforms = True
except ImportError:
    has_wtforms = False


JAVASCRIPT_LIBRARIES = frozenset(('auto', 'jquery', 'zepto'))
DEFAULT_JAVASCRIPT_LIBARY = 'jquery'

ICON_SETS = frozenset((
    'general',
    'general_enclosed',
    'accessibility',
    'social'
))


def check_wtforms():
    if not has_wtforms:
        raise RuntimeError(
            "Flask-Fundatio form rendering support is not available "
            "(could not import 'wtforms')")


def add_css_class(d, key, value):
    """Helper function to set or add a CSS class to a dict key"""
    if 'class' in d:
        d['class'] += ' error'
    else:
        d['class'] = 'error'


def field_kwargs_filter(d, field):
    check_wtforms()
    if field.errors:
        add_css_class(d, 'class', 'error')
    return d


def label_kwargs_filter(d, field):
    check_wtforms()
    if field.errors:
        add_css_class(d, 'class', 'error')
    return d


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

        icon_sets = app.config.setdefault('FUNDATIO_ICON_SETS', [])
        if set(icon_sets) - ICON_SETS:
            raise ValueError(
                "Invalid 'FUNDATIO_ICON_SETS' value in config; "
                "valid list values are: %s"
                % ', '.join(ICON_SETS))

        blueprint = Blueprint(
            'fundatio',
            __name__,
            static_folder='static',
            # XXX: specify explicit static url path to work around
            # https://github.com/mitsuhiko/flask/issues/348
            static_url_path='%s/foundation' % app.static_url_path,
            template_folder='templates',
        )

        blueprint.add_app_template_filter(
            field_kwargs_filter,
            name='_fundatio_form_field_kwargs')
        blueprint.add_app_template_filter(
            label_kwargs_filter,
            name='_fundatio_form_label_kwargs')

        app.register_blueprint(blueprint)
