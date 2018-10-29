FROM python:3.6-alpine

MAINTAINER Jc Din <ozknightwalker62@gmail.com>

WORKDIR /app

COPY requirements.txt .

RUN apk update && apk add --no-cache --virtual .build-deps \
    build-base gcc linux-headers python3-dev \
    && pip3 --no-cache-dir install -r requirements.txt \
    && find /usr/local -name '*.pyc' | xargs rm -rf \
    && apk del .build-deps

ENV PORT 8000

EXPOSE 8000

COPY . .

ENTRYPOINT ["./entrypoint.sh"]