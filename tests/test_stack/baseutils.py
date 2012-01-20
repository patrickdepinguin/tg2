import tg

class FakePackage(object):
    pass

default_config = {
        'debug': False,
        'package': FakePackage,
        'paths': {'root': None,
                         'controllers': None,
                         'templates': [],
                         'static_files': None},
        'db_engines': {},
        'tg.strict_tmpl_context':False,
        'buffet.template_engines': [],
        'buffet.template_options': {},
        'default_renderer':'genshi',
        'renderers':['json'],
        'render_functions':{'json':tg.render.render_json},
        'use_legacy_renderers':False,
        'use_sqlalchemy': False
}

class FakeRoutes(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['wsgiorg.routing_args'] = [None, {'controller':'root'}]
        environ['routes.url'] = None
        return self.app(environ, start_response)

class ControllerWrap(object):
    def __init__(self, controller):
        self.controller = controller

    def __call__(self, environ, start_response):
        app = self.controller()
        app.start_response = None
        return app(environ, start_response)