from __future__ import unicode_literals

import asyncio
import uvloop

from signal import signal, SIGINT

from app.settings import app, RUNNER_CONFIG

if __name__ == '__main__':
    from app import urls

    asyncio.set_event_loop(uvloop.new_event_loop())
    # app.run(**RUNNER_CONFIG)
    server = app.create_server(**RUNNER_CONFIG)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(server)
    signal(SIGINT, lambda s, f: loop.stop())
    try:
        loop.run_forever()
    except Exception:
        loop.stop()
