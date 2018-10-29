#!/bin/sh

gunicorn -b :$PORT manage:app --worker-class sanic.worker.GunicornWorker --max-requests 100