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
from demo.utils.sampleJSON import hugeObj,hugeObjPlus,transction
from faker import Faker
from faker.providers import company
from flask import jsonify
from flask import request,Response
import datetime;
import enum
import uuid

#pull values from env vars
environment = os.environ['ENV']
# req_timeout_value = int(os.environ['LOAD_GEN_REQUEST_TIMEOUT']) if os.environ['LOAD_GEN_REQUEST_TIMEOUT'] else 50
# api_endpoint = 'http://app:5000/api/v1/'
api_endpoint = os.environ['API_ENDPOINT']
# https://faker.readthedocs.io/en/master/
fake = Faker()
fake.add_provider(company)

# Scrape data into Prometheus
import six
from itertools import chain
from locust import stats as locust_stats, runners as locust_runners
from locust import User, task, events
from prometheus_client import Metric, REGISTRY, exposition

# Function to scrape statistics from Locust and make it avaiable on Prometheus/Grafana
# This locustfile adds an external web endpoint to the locust master, and makes it serve as a prometheus exporter.
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


"""Functions for tasks to be used in the Task set"""

def get_id(pattern):
    #use scan on the key level 
    try:
        resp = requests.get(api_endpoint + 'keys?pattern=' + pattern, verify=False)
        r = resp.json()
        keys = r.get('json')
        return keys
    except Exception as e:
        return {'error':str(e)}

fields = ['age','name','address','location']
BasicUserTestSet = get_id('basicUser')
AdvancedUserTestSet = get_id('advancedUser')
hugeObjTestSet = get_id('redisJSON')
hugeObjFields = ['damage_relations', 'move_damage_class', 'pokemon']
stringTestSet = get_id('stringJSON')
hashTestSet = get_id('hash')
nestedFields = ['damage_relations.double_damage_from[0].name', 'names[0].language.name']

""" Build the TaskSet """
class testOnJSONSet(TaskSet):
    @tag('add_string')
    # @task(3)
    def add_static_huge_string(self):
        json_doc = json.dumps(transction)
        self.client.post('/api/v1/string',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_string')

    @tag('add_json')
    @task(3)
    def add_huge_json(self):
        json_doc = json.dumps(transction)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_json')


class testOnJSONGet(TaskSet):
    @tag('get_string')
    # @task(2)
    def get_static_huge_string(self):        
        self.client.get('/api/v1/string/{}'.format(random.choice(stringTestSet)), timeout=50, name='/api/v1/get_string')

    @tag('get_json')
    @task(2)
    def get_huge_json(self):
        self.client.get('/api/v1/doc/{}'.format(random.choice(hugeObjTestSet)), timeout=50, name='/api/v1/get_json')

class testOnChangeJSON(TaskSet):
    @tag('updateField_json')
    @task(2)
    def updateField_huge_json(self):
        update = {
            'key': random.choice(hugeObjTestSet),
            'field': 'generation',
            'str': 'generation-X'
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField_json')

    @tag('updateField_string')
    @task(2)
    def updateField_huge_string(self):
        update = {
            'key': random.choice(stringTestSet),
            'field': 'generation',
            'str': 'generation-X'
        }
        self.client.put('/api/v1/string/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField_string')

    @tag('update_nested_Field_json')
    @task(2)
    def update_nested_Field_json(self):
        update = {
            'key': random.choice(hugeObjTestSet),
            'field': 'damage_relations.double_damage_from[0].name',
            'str': 'lightening'
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/update_nested_Field_json')

    @tag('json_append_string')
    #@task(2)
    def json_append_string(self):
        update = {
            'key': random.choice(hugeObjTestSet),
            'field': 'damage_relations.double_damage_from[0].name',
            'str': ' & Jumping'}

        self.client.put('/api/v1/redisjson/append',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/json_append_string')

            
    @tag('NumIncrby')
    @task(1)
    def hugeObj_num_incr_by(self):
        fieldNum = {
            'key': random.choice(hugeObjTestSet),
            'field': 'pokemon[0].slot',
            'num': random.randint(1,10)
        }
        self.client.put('/api/v1/redisjson/increby',
            data=json.dumps(fieldNum),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/numbIncryBy')

class moreJSONTest(TaskSet):
    @tag('get_json_by_key_and_field')
    @task(2)
    def get_json_by_key_and_field(self):
        self.client.get('/api/v1/subdoc/{}/{}'.format(random.choice(hugeObjTestSet), random.choice(hugeObjFields)), timeout=50, name='/api/v1/get_json_by_key_and_field')
        # self.client.cookies.clear()

    @tag('get_string_by_key_and_field')
    @task(2)
    def get_string_by_key_and_field(self):
        self.client.get('/api/v1/string/{}/{}'.format(random.choice(stringTestSet), random.choice(hugeObjFields)), timeout=50, name='/api/v1/get_string_by_key_and_field')
        # self.client.cookies.clear()


    @tag('get_nested_json_by_key_and_field')
    @task(2)
    def get_json(self):
        self.client.get('/api/v1/subdoc/{}/{}'.format(random.choice(hugeObjTestSet), random.choice(nestedFields)), timeout=50, name='/api/v1/get_nested_json')
        # self.client.cookies.clear()

class testOnRandomGet(TaskSet):
    """ task functions to be used in the TaskSet """
    @tag('getJsonByKey')
    @task(3)
    def get_json_by_key(self):
        self.client.get('/api/v1/doc/{}'.format(random.choice(AdvancedUserTestSet)), timeout=50, name='/api/v1/getJsonByKey')
        # self.client.cookies.clear()

    @tag('getField')
    # @task(3)
    def get_json_by_key_and_field(self):
        self.client.get('/api/v1/subdoc/{}/{}'.format(random.choice(BasicUserTestSet), random.choice(fields)), timeout=50, name='/api/v1/getValueByKeyAndFields')
        # self.client.cookies.clear()

    @tag('getListOfFieldsByKey')
    #@task(3)
    def get_list_of_fields_by_key(self):
        self.client.get('/api/v1/fields/{}'.format(random.choice(AdvancedUserTestSet)), timeout=50, name='/api/v1/examples/getListOfFieldsByKey')

class testOnRandomJson(TaskSet):
    @tag('add_random_small_json')
    @task(3)
    def add_random_small_json(self):
        json_doc = {
            'id':   "basicUser:" + str(uuid.uuid4()),
            'name': fake.name(),
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

class testOnPutRandom(TaskSet):
    @tag('updateField_json')
    #@task(2)
    def update_field(self):
        update = {
            'key': random.choice(AdvancedUserTestSet),
            'field': 'name',
            'str': 'Albert Z'
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField')

    @tag('update_nested_field_json')
    @task(2)
    def update_field_nested(self):
        update = {
            'key': random.choice(AdvancedUserTestSet),
            'field': 'contract.name',
            'str': 'Redis Lab'
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/update_field_nested')

    @tag('appendString')
    # @task(1)
    def append_string(self):
        append = {
            'key': random.choice(AdvancedUserTestSet),
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
        fieldNum = {
            'key': random.choice(BasicUserTestSet),
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
    #@task(1)
    def num_multi_by(self):
        fieldNum = {
            'key': random.choice(BasicUserTestSet),
            'field': 'age',
            'num': random.randint(1,10)
        }
        self.client.put('/api/v1/redisjson/multiby',
            data=json.dumps(fieldNum),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/numMultiBy')
        # self.client.cookies.clear()

class hashvsjsonPost(TaskSet):
    @tag('hashvsjsonPost')
    @task(1)
    def postHash(self):
        json_doc = {
            'name': fake.name(),
            'age': fake.random_int(min=0, max=100),
            'location': str(fake.latitude()),
            'address': fake.street_address()
        }
        json_doc = json.dumps(json_doc)

        self.client.post('/api/v1/hash',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/postHash')

    @tag('postJSON')
    @task(1)
    def postJSON(self):
        json_doc = {
            'name': fake.name(),
            'age': fake.random_int(min=0, max=100),
            'location': str(fake.latitude()),
            'address': fake.street_address()
        }
        json_doc = json.dumps(json_doc)

        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/postJSON')

class hashvsjsonGet(TaskSet):
    @tag('getHash')
    @task(1)
    def getHash(self):
        self.client.get('/api/v1/hash/{}'.format(random.choice(hashTestSet), timeout=50, name='/api/v1/get_hash'),
            name='/api/v1/get')

    @tag('getJSON')
    @task(1)
    def getJson(self):
        self.client.get('/api/v1/doc/{}'.format(random.choice(hugeObjTestSet)), timeout=50, name='/api/v1/get_json')

    @tag('getHashField')
    @task(1)
    def get_hash_by_key_and_field(self):
        self.client.get('/api/v1/hash/{}/{}'.format(random.choice(hashTestSet), random.choice(fields)), timeout=50, name='/api/v1/getFieldValueHash')
        # self.client.cookies.clear()

    @tag('getJSONField')
    @task(1)
    def get_json_by_key_and_field(self):
        self.client.get('/api/v1/subdoc/{}/{}'.format(random.choice(hugeObjTestSet), random.choice(fields)), timeout=50, name='/api/v1/getFieldValueJSON')
        # self.client.cookies.clear()

class hashvsjsonUpdate(TaskSet):
    @tag('updateHash')
    @task(1)
    def updateHash(self):
        update = {
            'key': random.choice(hashTestSet),
            'field': 'address',
            'str': fake.street_address()
        }
        self.client.put('/api/v1/hash/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField_hash')


    @tag('updateJSON')
    @task(1)
    def updateJson(self):
        update = {
            'key': random.choice(hugeObjTestSet),
            'field': 'address',
            'str': fake.street_address()
        }
        self.client.put('/api/v1/redisjson/update',
            data=json.dumps(update),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/updateField_redisjson')

class nestedJSON(TaskSet):
    @tag('jsonPOST')
    @task(1)
    def postJSONNested(self):
        ct = datetime.datetime.now()
        nested_json = {
            'id': "user:" + str(uuid.uuid4()),
            'org_id': "redis:" + str(uuid.uuid4()),
            'activeStatus': fake.boolean(chance_of_getting_true=25),
            'age': fake.random_int(min=0, max=100),
            'data':{
                'id': fake.company(),
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'external_json': 
                { 
                    "id": "external:"+str(uuid.uuid4()),
                    "type": "PushEvent",
                    "payload": {
                        "push_id": "payload" + str(uuid.uuid4()),
                        "size": fake.random_int(min=0, max=50),
                        "distinct_size": fake.random_int(min=0, max=10),
                        "ref": "refs/heads/master"
                     },
                    "public": fake.boolean(chance_of_getting_true=85),
                    "created_at": ct.timestamp(),
                }, 
                'foreign_key': str(fake.random_int(min=0, max=1000))
            },
            'metadata': {
                'agent':{
                    "name": "agent:" + str(uuid.uuid4()),
                    "addr": fake.ipv4(),
                    "email": fake.safe_email(),
                    "port": fake.port_number(),
                    "tags": {
                        "dc": fake.random_int(min=0, max=10),
                        "role": str(fake.job())
                    },
                    "status": fake.boolean(chance_of_getting_true=25),
                },
                'provenance':
                {
                    "resourceType" : "StructureDefinition",
                    "id" : "provenance"+ str(uuid.uuid4()),
                    "lastUpdated" : ct.timestamp(),
                    "extension" : [{
                        "url" : fake.uri(),
                        "valueCode" : fake.random_int(min=0, max=10)
                    },
                    {
                        "url" : fake.uri(),
                        "valueCode" : fake.random_int(min=0, max=10)
                    },
                    {
                        "url" : fake.uri(),
                        "valueInteger" : fake.random_int(min=0, max=10)
                    },
                    {
                        "url" : fake.uri(),
                        "valueCode" : fake.random_int(min=0, max=10)
                    }],
                    "countryCode" : fake.country_code(),
                }
            }
        }
    
        self.client.post('/api/v1/redisjson',
            data=json.dumps(nested_json,use_decimal=True, indent=4, sort_keys=True, default=str),
            headers={'Content-Type': 'application/json'},
            timeout=50,
            name='/api/v1/add_random_big_json')
        # self.client.cookies.clear()




""" Generate the load """

class GenerateLoad(FastHttpUser):
    # connection_timeout=100
    # network_timeout=50
    tasks = [nestedJSON]


