from __future__ import unicode_literals

from app.core.views import TemplateView


class HomeView(TemplateView):
    template_name = 'homepage.html'

    def get_context_data(self, *args, **kwargs):
        return {'title': 'Homepage'}
