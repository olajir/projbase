FROM python:latest

RUN mkdir -p /usr/src/app/base
WORKDIR /usr/src/app/base
COPY . /usr/src/app/base

RUN pip install --no-cache-dir ./imgbase
