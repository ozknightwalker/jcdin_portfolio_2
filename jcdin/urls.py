from __future__ import unicode_literals

from app.settings import app

from .views import *

app.add_route(HomeView.as_view(), '/')
