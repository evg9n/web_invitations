FROM python:3.10.12-alpine

WORKDIR /app

USER root

RUN apk add --no-cache libpq postgresql-dev build-base

RUN python -m pip install --upgrade pip

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn its_smeta.wsgi:application --bind 0.0.0.0:8000
