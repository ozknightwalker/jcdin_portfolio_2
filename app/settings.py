from __future__ import unicode_literals

import os

from sanic import Sanic

app = Sanic(__name__)

app.config.from_object(dict(
    KEEP_ALIVE=False,
    HOST=os.environ.get('HOST', '0.0.0.0'),
    PORT=os.environ.get('PORT', 8000),
))
