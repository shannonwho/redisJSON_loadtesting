#Multi-stage dockerfiles 

FROM ubuntu:18.04 AS base

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev git

WORKDIR /app

COPY . /app
#layer caching
# COPY package.json pip3.lock ./
RUN pip3 install -r requirements.txt
ADD . /app/
EXPOSE 5000
CMD gunicorn --chdir ./demo --workers 4 --threads 2 -b 0.0.0.0:5000 'demo.app:app'


FROM locustio/locust AS test

WORKDIR /test
COPY . /test

RUN pip3 install -r locust/requirements.txt 

ADD . /test/