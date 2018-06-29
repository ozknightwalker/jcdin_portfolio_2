from __future__ import unicode_literals

from sanic import response

from app.core.views import TemplateView, View


class HomeView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, *args, **kwargs):
        return {'title': 'Homepage'}


class ServiceWorkerView(View):
    methods = ('get',)

    async def get(self, *args, **kwargs):
        return await self.render_response()

    async def render_response(self):
        return await response.file(
            './jcdin/static/js/sw.js',
            headers={'Content-Type': 'application/javascript'})


class WebManifestView(View):
    methods = ('get',)

    async def get(self, *args, **kwargs):
        return await self.render_response()

    async def render_response(self):
        return await response.file(
            './jcdin/static/manifest.webmanifest',
            headers={'Content-Type': 'application/manifest+json'})
