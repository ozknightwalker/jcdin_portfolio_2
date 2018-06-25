from __future__ import unicode_literals

import os
from multiprocessing import cpu_count

from sanic import Sanic

from app.core.middlewares import Compressor

DEFAULT_MIMETYPES = (
    'text/html',
    'text/css',
    'text/xml',
    'application/json',
    'application/javascript',
)

COMPRESS_SETTINGS = dict(
    COMPRESS_LEVEL=int((os.environ.get('COMPRESS_LEVEL', 6))),
    COMPRESS_MIN_SIZE=int((os.environ.get('COMPRESS_MIN_SIZE', 500))),
    COMPRESS_MIMETYPES=set(os.environ.get(
        'COMPRESS_MIMETYPES', DEFAULT_MIMETYPES)),
)

app = Sanic(__name__)

app.config.from_object(dict(
    KEEP_ALIVE=bool(os.environ.get('KEEP_ALIVE', False)),
))
app.config.update(COMPRESS_SETTINGS)
Compressor(app)

app.static('/static', './dist')
app.url_for('static', filename='app.js')
app.url_for('static', filename='vendors.js')

RUNNER_CONFIG = {
    'host': os.environ.get('HOST', '0.0.0.0'),
    'port': int(os.environ.get('PORT', 8000)),
    'debug': bool(os.environ.get('DEBUG', False)),
    # 'workers': int(cpu_count() / 2),
}
