from __future__ import unicode_literals

import os
from multiprocessing import cpu_count

from sanic import Sanic

app = Sanic(__name__)

app.config.from_object(dict(
    KEEP_ALIVE=os.environ.get('KEEP_ALIVE', True),
    HOST=os.environ.get('HOST', '0.0.0.0'),
    PORT=os.environ.get('PORT', 8000),
    WORKERS=os.environ.get('WORKERS', cpu_count()),
    DEBUG=os.environ.get('DEBUG', False),
))
