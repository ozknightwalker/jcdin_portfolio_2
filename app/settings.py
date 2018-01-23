from __future__ import unicode_literals

import os
from multiprocessing import cpu_count

from sanic import Sanic

from app.core.compressor import Compress

app = Sanic(__name__)
Compress(app)

app.config.from_object(dict(
    KEEP_ALIVE=bool(os.environ.get('KEEP_ALIVE', False)),
    COMPRESS_LEVEL=int((os.environ.get('COMPRESS_LEVEL', 6))),
    COMPRESS_MIN_SIZE=int((os.environ.get('COMPRESS_MIN_SIZE', 500))),
))

RUNNER_CONFIG = {
    'host': os.environ.get('HOST', '0.0.0.0'),
    'port': int(os.environ.get('PORT', 8000)),
    'debug': bool(os.environ.get('DEBUG', True)),
    'workers': int(cpu_count()),
}
