from __future__ import unicode_literals

from sanic.views import HTTPMethodView
from sanic.response import text


class HomeView(HTTPMethodView):

    async def get(self, request):
        return text('Homepage')
