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
ENTRYPOINT [ "python3" ]
CMD [ "./demo/app.py" ]



FROM locustio/locust AS test

WORKDIR /test
COPY . /test

RUN pip3 install -r locust/requirements.txt 

ADD . /test/