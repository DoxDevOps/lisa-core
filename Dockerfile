# syntax=docker/dockerfile:1
FROM python:3.8.11-alpine3.13
WORKDIR /lisa-core

ADD requirements.txt requirements.txt
RUN set -ex \
    && apk add --no-cache --virtual .build-deps gcc python3-dev musl-dev postgresql-dev build-base \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && /env/bin/pip install --no-cache-dir -r requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
    | sort -u \
    | xargs -r apk info --installed \
    | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

EXPOSE 80
COPY . .
CMD ["python3", "app.py"]
