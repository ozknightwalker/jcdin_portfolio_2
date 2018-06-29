from __future__ import unicode_literals

from app.settings import app

from .views import *

app.add_route(HomeView.as_view(), '/')
app.add_route(ServiceWorkerView.as_view(), '/service-worker.js')
app.add_route(WebManifestView.as_view(), '/manifest.webmanifest')
