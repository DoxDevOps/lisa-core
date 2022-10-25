# syntax=docker/dockerfile:1
FROM python:3.6.9-alpine
WORKDIR /lisa-core

RUN apk --update --upgrade add --no-cache  gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 80
COPY . .
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]