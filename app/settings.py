from __future__ import unicode_literals

import os
from multiprocessing import cpu_count

from sanic import Sanic

app = Sanic(__name__)

app.config.from_object(dict(
    KEEP_ALIVE=bool(os.environ.get('KEEP_ALIVE', False)),
))

RUNNER_CONFIG = {
    'host': os.environ.get('HOST', '0.0.0.0'),
    'port': int(os.environ.get('PORT', 8000)),
    'debug': bool(os.environ.get('DEBUG', True)),
    'workers': int(cpu_count()),
}
