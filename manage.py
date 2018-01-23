from __future__ import unicode_literals

from app.settings import app, RUNNER_CONFIG

if __name__ == '__main__':
    from app import urls
    app.run(**RUNNER_CONFIG)
