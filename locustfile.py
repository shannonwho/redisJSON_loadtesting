from locust import HttpUser, User, TaskSet, task, web, runners, between, tag
# from locust.runners import MasterLocustRunner
from locust.contrib.fasthttp import FastHttpUser
from locust.stats import sort_stats
from locust.util.rounding import proper_round
# import json
from itertools import chain
try:
    # >= Py3.2
    from html import escape
except ImportError:
    # < Py3.2
    from cgi import escape
import simplejson as json
import os
import random
import string
import requests
from rejson import Client, Path
from demo.utils.sampleJSON import smallObj,bigObj
from faker import Faker
from faker.providers import company
from flask import jsonify
from flask import request,Response
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import date
import enum
import uuid

#pull values from env vars
environment = os.environ['ENV']
req_timeout_value = int(os.environ['LOAD_GEN_REQUEST_TIMEOUT']) if os.environ['LOAD_GEN_REQUEST_TIMEOUT'] else 50
api_endpoint = 'http://app:5000/api/v1/'

# https://faker.readthedocs.io/en/master/
fake = Faker()
fake.add_provider(company)

# Scrape data into Prometheus
import six
from itertools import chain
from locust import stats as locust_stats, runners as locust_runners
from locust import User, task, events
from prometheus_client import Metric, REGISTRY, exposition

# This locustfile adds an external web endpoint to the locust master, and makes it serve as a prometheus exporter.
# Runs it as a normal locustfile, then points prometheus to it.
# locust -f prometheus_exporter.py --master

# Lots of code taken from [mbolek's locust_exporter](https://github.com/mbolek/locust_exporter), thx mbolek!


class LocustPrometheusCollector(object):
    registry = REGISTRY

    def __init__(self, environment, runner):
        self.environment = environment
        self.runner = runner

    def collect(self):
        # collect metrics only when locust runner is spawning or running.
        runner = self.runner

        if runner and runner.state in (locust_runners.STATE_SPAWNING, locust_runners.STATE_RUNNING):
            stats = []
            for s in chain(locust_stats.sort_stats(runner.stats.entries), [runner.stats.total]):
                stats.append({
                    "method": s.method,
                    "name": s.name,
                    "num_requests": s.num_requests,
                    "num_failures": s.num_failures,
                    "avg_response_time": s.avg_response_time,
                    "min_response_time": s.min_response_time or 0,
                    "max_response_time": s.max_response_time,
                    "current_rps": s.current_rps,
                    "median_response_time": s.median_response_time,
                    "ninetieth_response_time": s.get_response_time_percentile(0.9),
                    # only total stats can use current_response_time
                    #"current_response_time_percentile_95": s.get_current_response_time_percentile(0.95),
                    "avg_content_length": s.avg_content_length,
                    "current_fail_per_sec": s.current_fail_per_sec
                })

            # perhaps StatsError.parse_error in e.to_dict only works in python slave, take notices!
            errors = [e.to_dict() for e in six.itervalues(runner.stats.errors)]

            metric = Metric('locust_user_count', 'Swarmed users', 'gauge')
            metric.add_sample('locust_user_count', value=runner.user_count, labels={})
            yield metric
            
            metric = Metric('locust_errors', 'Locust requests errors', 'gauge')
            for err in errors:
                metric.add_sample('locust_errors', value=err['occurrences'],
                                  labels={'path': err['name'], 'method': err['method'],
                                          'error': err['error']})
            yield metric

            is_distributed = isinstance(runner, locust_runners.MasterRunner)
            if is_distributed:
                metric = Metric('locust_slave_count', 'Locust number of slaves', 'gauge')
                metric.add_sample('locust_slave_count', value=len(runner.clients.values()), labels={})
                yield metric

            metric = Metric('locust_fail_ratio', 'Locust failure ratio', 'gauge')
            metric.add_sample('locust_fail_ratio', value=runner.stats.total.fail_ratio, labels={})
            yield metric

            metric = Metric('locust_state', 'State of the locust swarm', 'gauge')
            metric.add_sample('locust_state', value=1, labels={'state': runner.state})
            yield metric

            stats_metrics = ['avg_content_length', 'avg_response_time', 'current_rps', 'current_fail_per_sec',
                             'max_response_time', 'ninetieth_response_time', 'median_response_time', 'min_response_time',
                             'num_failures', 'num_requests']

            for mtr in stats_metrics:
                mtype = 'gauge'
                if mtr in ['num_requests', 'num_failures']:
                    mtype = 'counter'
                metric = Metric('locust_stats_' + mtr, 'Locust stats ' + mtr, mtype)
                for stat in stats:
                    # Aggregated stat's method label is None, so name it as Aggregated
                    # locust has changed name Total to Aggregated since 0.12.1
                    if 'Aggregated' != stat['name']:
                        metric.add_sample('locust_stats_' + mtr, value=stat[mtr],
                                          labels={'path': stat['name'], 'method': stat['method']})
                    else:
                        metric.add_sample('locust_stats_' + mtr, value=stat[mtr],
                                          labels={'path': stat['name'], 'method': 'Aggregated'})
                yield metric


@events.init.add_listener
def locust_init(environment, runner, **kwargs):
    print("locust init event received")
    if environment.web_ui and runner:
        @environment.web_ui.app.route("/metrics")
        def prometheus_exporter():
            registry = REGISTRY
            encoder, content_type = exposition.choose_encoder(request.headers.get('Accept'))
            if 'name[]' in request.args:
                registry = REGISTRY.restricted_registry(request.args.get('name[]'))
            body = encoder(registry)
            return Response(body, content_type=content_type)
        REGISTRY.register(LocustPrometheusCollector(environment, runner))




"""Functions for tasks to be used in the Tasl set"""

def get_id(pattern):
    #use scan on the key level 
    try:
        resp = requests.get(api_endpoint + 'keys?pattern=' + pattern, verify=False)
        r = resp.json()
        keys = r.get('json')
        return keys
    except Exception as e:
        return {'error':str(e)}

fields = ['id','name','address','location']


""" Build the TaskSet """
class testOnPost(TaskSet):
    @tag('add_static_small_json')
    @task(3)
    def add_static_small_json(self):
        json_doc = json.dumps(smallObj)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_static_small_json')
        # self.client.cookies.clear()

    @tag('add_random_small_json')
    @task(3)
    def add_random_small_json(self):
        json_doc = {
            'id':   "basicUser:" + str(uuid.uuid4()),
            'name': fake.company(),
            'age': fake.random_int(min=0, max=100),
            'location': str(fake.latitude()),
            'address': fake.street_address()
        }
        json_doc = json.dumps(json_doc)

        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_random_small_json')
        # self.client.cookies.clear()

    @tag('add_static_big_json')
    @task(3)
    def add_static_big_json(self):
        json_doc = json.dumps(bigObj)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_static_big_json')
        # self.client.cookies.clear()

    @tag('add_random_big_json')
    @task(3)
    def add_random_big_json(self):
        nested_json = {
            'id': "advancedUser:" + str(uuid.uuid4()),
            'name': fake.company(),
            'activeStatus': False,
            'age': str(fake.random_int(min=0, max=100)),
            'location':{
                'latitude': fake.latitude(),
                'longitude':fake.longitude()
            },
            'address': [
                fake.street_address(), 
                fake.street_address(), 
                fake.street_address()]
            }
        self.client.post('/api/v1/redisjson',
            data=json.dumps(nested_json,use_decimal=True),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_random_big_json')
        # self.client.cookies.clear()

    @tag('add_static_simple_hash')
    @task(3)
    def add_static_simple_hash(self):
        json_doc = json.dumps(smallObj)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_static_simple_hash')
        # self.client.cookies.clear()

    @tag('add_random_simple_hash')
    @task(3)
    def add_random_simple_hash(self):
        json_doc = {
            'id':   "simpleHash:" + str(uuid.uuid4()),
            'name': fake.company(),
            'age': fake.random_int(min=0, max=100),
            'location': str(fake.latitude()),
            'address': fake.street_address()
        }
        json_doc = json.dumps(json_doc)

        self.client.post('/api/v1/hash',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_random_simple_hash')
        # self.client.cookies.clear()

    @tag('add_static_big_hash')
    @task(3)
    def add_static_big_json_hash(self):
        json_doc = json.dumps(bigObj)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_static_big_hash')
        # self.client.cookies.clear()

    @tag('add_random_big_hash')
    @task(3)
    def add_random_big_hash(self):
        nested_json = {
            'id': "advancedUser:" + str(uuid.uuid4()),
            'name': fake.company(),
            'activeStatus': False,
            'age': str(fake.random_int(min=0, max=100)),
            'contract':
                {
                    'name': fake.company(),
                    'occupation': 'Solution Architect',
                    'zipCode': "92603"
                },
            'location':[
                {
                'latitude': fake.latitude(),
                'longitude':fake.longitude()
                },
                {
                'latitude': fake.latitude(),
                'longitude':fake.longitude()
                },
                {
                'latitude': fake.latitude(),
                'longitude':fake.longitude()
                }],
            'address': [
                fake.street_address(), 
                fake.street_address(), 
                fake.street_address()]
        }
        json_doc = json.dumps(nested_json)
        self.client.post('/api/v1/hash',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_random_big_hash')
        # self.client.cookies.clear()


class testOnGet(TaskSet):
    """ task functions to be used in the TaskSet """

    @tag('getJSONByKey')
    @task(3)
    def get_json_by_key(self):
        id = get_id('basicUser')
        self.client.get('/api/v1/doc/{}'.format(random.choice(id)), timeout=50, name='/api/v1/getJsonByKey')
        # self.client.cookies.clear()


    @tag('getHashByKey')
    #@task(3)
    def get_hash_by_key(self):
        id = get_id('simpleHash')
        self.client.get('/api/v1/hash/{}'.format(random.choice(id)), timeout=50, name='/api/v1/getHashByKey')
        # self.client.cookies.clear()


    @tag('getField')
    @task(3)
    def get_json_by_key_and_field(self):
        id= get_id('basicUser')
        self.client.get('/api/v1/subdoc/{}/{}'.format(random.choice(id), random.choice(fields)), timeout=50, name='/api/v1/getValueByKeyAndFields')
        # self.client.cookies.clear()

    @tag('getListOfFieldsByKey')
    @task(3)
    def get_list_of_fields_by_key(self):
        id = get_id('advancedUser')
        self.client.get('/api/v1/fields/{}'.format(random.choice(id)), timeout=50, name='/api/v1/examples/getListOfFieldsByKey')
        # self.client.cookies.clear()


class testOnPut(TaskSet):
    @tag('updateField_json')
    @task(2)
    def update_field(self):
        id = get_id('advancedUser:')
        update = {
            'key': random.choice(id),
            'field': 'name',
            'str': 'Redis Lab'
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField_json')

    @tag('update_nested_field_json')
    @task(2)
    def update_field(self):
        id = get_id('advancedUser')
        update = {
            'key': random.choice(id),
            'field': 'name',
            'str': 'Redis Lab'
        }
        self.client.put('/api/v1/hash/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField_hash')

    @tag('appendString')
    @task(1)
    def append_string(self):
        id = get_id('basicUser')
        append = {
            'key': random.choice(id),
            'field': 'name',
            'str': ' Hu'
        }
        self.client.put('/api/v1/redisjson/append',
            data=json.dumps(append),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/appendString')
        # self.client.cookies.clear()

    @tag('NumIncrby')
    @task(1)
    def num_incr_by(self):
        id = get_id('basicUser')
        fieldNum = {
            'key': random.choice(id),
            'field': 'age',
            'num': random.randint(1,10)
        }
        self.client.put('/api/v1/redisjson/increby',
            data=json.dumps(fieldNum),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/numbIncryBy')
        # self.client.cookies.clear()

    @tag('NumMultiby')
    @task(1)
    def num_multi_by(self):
        id = get_id('basicUser')
        fieldNum = {
            'key': random.choice(id),
            'field': 'age',
            'num': random.randint(1,10)
        }
        self.client.put('/api/v1/redisjson/multiby',
            data=json.dumps(fieldNum),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/numMultiBy')
        # self.client.cookies.clear()

""" Generate the load """

class GenerateLoad(FastHttpUser):
    connection_timeout=100
    network_timeout=50
    tasks = [testOnPost,testOnPut]
    # min_wait = 5000
    # max_wait = 20000

