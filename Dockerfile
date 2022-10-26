# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /lisa-core-docker
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]