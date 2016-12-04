FROM python:latest

RUN mkdir -p /tmp
WORKDIR /tmp
COPY . /tmp

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir .

RUN rm -r *
