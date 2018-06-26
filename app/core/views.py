from __future__ import unicode_literals

from sanic.response import html
from sanic.views import HTTPMethodView
from sanic import exceptions

from app.template import template_env
from app.core.exceptions import ImproperlyConfigured


class View(HTTPMethodView):
    methods = ()

    def dispatch_request(self, request):
        if request.method.lower() not in self.methods:
            raise NotFound("Method Not Allowed", status_code=405)
        return super().dispatch_request(request)


class ContextMixin(object):

    def get_context_data(self, *args, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        return kwargs


class TemplateResponseMixin(object):
    template_name = None

    def get_template(self):
        if self.template_name is None:
            error_msg = '{} `template_name` is not provided'.format(
                self.__class__.__name__)
            raise ImproperlyConfigured(error_msg)
        try:
            template = template_env.get_template(self.template_name)
        except Exception:
            error_msg = 'Template {} not found'.format(self.template_name)
            raise ImproperlyConfigured(error_msg)
        else:
            return template

    async def render_response(self, context):
        template = self.get_template()
        rendered_template = await template.render_async(context)
        return html(rendered_template)


class TemplateView(TemplateResponseMixin, ContextMixin, View):
    methods = ('get',)

    async def get(self, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        return await self.render_response(context)
