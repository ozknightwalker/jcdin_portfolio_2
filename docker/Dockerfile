FROM python:3.6-alpine

MAINTAINER Jc Din <ozknightwalker62@gmail.com>

# update package inages and install nodejs, python3-dev and gcc
RUN ["apk", "add", "--update", "--no-cache", "build-base", "linux-headers", "python3-dev", "gcc"]

WORKDIR /app

COPY requirements.txt .

RUN ["pip3", "install", "--no-cache-dir", "-r", "./requirements.txt"]

ENV PORT 8000

EXPOSE 8000

COPY . ./

CMD exec gunicorn -b :$PORT manage:app --worker-class sanic.worker.GunicornWorker --max-requests 100
