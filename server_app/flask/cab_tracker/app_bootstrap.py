__author__ = 'cabtracker'


def register_blueprints(app, blueprints):
    """

    """

    for key, value in blueprints.iteritems():
        module = __import__("view.%s" % key,
                            locals(), globals(), ['app_route', ])
        app.register_blueprint(getattr(module, 'app_route'))

