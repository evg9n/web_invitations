FROM python:3.10.12-alpine

WORKDIR /app

RUN apk add --no-cache libpq postgresql-dev build-base

RUN python -m pip install --upgrade pip

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8000