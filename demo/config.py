import os

"""
Pull all environment variables required.

Local: passed via docker-compose and configuration files

Cloud: ansible generates dynamic environment configuration files and passes those to containers run

Use this model to pass any additional environment variables into the APP

"""

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']
REDIS_PASSWORD = os.environ['REDIS_PASSWORD']
ENV = os.environ['ENV']


# LOCUST_URL = os.environ['LOCUST_URL']
# LOCUST_CLIENTS = os.environ['LOCUST_CLIENTS']
# LOCUST_HATCH_RATE = os.environ['LOCUST_HATCH_RATE']
# CUSTOMIZE_CLIENT_COUNT = os.environ['CUSTOMIZE_CLIENT_COUNT']

