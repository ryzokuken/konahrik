from flask import request

from opentracing_instrumentation.client_hooks.requests import install_patches
from flask_opentracing import FlaskTracer
from jaeger_client import Config
from opentracing_instrumentation.request_context import RequestContextManager


class TracingMiddleware(object):
    def __init__(self, app, name):
        self.app = app.wsgi_app
        self.fapp = app
        self.name = name

        self.tracer = self.initialize_tracer()
        self.ftracer = FlaskTracer(self.tracer, False, app)

        install_patches()

    def __call__(self, environ, start_response):
        with self.fapp.request_context(environ):
            parent_span = self.ftracer.get_span(request)
            with self.tracer.start_span(self.name, child_of=parent_span) as span:
                with RequestContextManager(span=span):
                    return self.app(environ, start_response)

    def initialize_tracer(self):
        config = Config(
            config={
                'sampler': {'type': 'const', 'param': 1},
                'local_agent': {'reporting_host': 'jaeger'}
            },
            service_name=self.name
        )
        return config.initialize_tracer()
