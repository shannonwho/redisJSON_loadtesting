import os

"""
Pull all environment variables required.

Local: passed via docker-compose and configuration files

Cloud: ansible generates dynamic environment configuration files and passes those to containers run

Use this model to pass any additional environment variables into the APP

"""

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

ENV = os.environ['ENV']



# CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT']
# CACHE_KEY_PREFIX = os.environ['CACHE_KEY_PREFIX']
# CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
# CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']

# REDIS_CONNECTION_URL = f'redis://{CACHE_REDIS_HOST}:{CACHE_REDIS_PORT}'

# LOCUST_URL = os.environ['LOCUST_URL']
# LOCUST_CLIENTS = os.environ['LOCUST_CLIENTS']
# LOCUST_HATCH_RATE = os.environ['LOCUST_HATCH_RATE']
# CUSTOMIZE_CLIENT_COUNT = os.environ['CUSTOMIZE_CLIENT_COUNT']
# ENV = os.environ['ENV']

