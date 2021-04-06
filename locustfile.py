from locust import HttpUser, User, TaskSet, task, web, runners, between, tag
# from locust.runners import MasterLocustRunner
from locust.stats import sort_stats
# import json
import simplejson as json
import os
import random
import string
import requests
from rejson import Client, Path
from demo.utils.sampleJSON import smallObj,bigObj

from faker import Faker
from faker.providers import company
from datetime import time
from datetime import datetime
from datetime import timedelta
from datetime import date
import enum
import uuid


#In order for json.dump works with nested array
def to_serializable(val):
    """JSON serializer for objects not serializable by default"""
    if isinstance(val, (datetime, date, time)):
        return val.isoformat()
    elif isinstance(val, enum.Enum):
        return val.value
    elif hasattr(val, '__dict__'):
        return val.__dict__
    return val


#pull values from env vars
environment = os.environ['ENV']
req_timeout_value = int(os.environ['LOAD_GEN_REQUEST_TIMEOUT']) if os.environ['LOAD_GEN_REQUEST_TIMEOUT'] else 20
api_endpoint = 'http://app:5000/api/v1/'

# https://faker.readthedocs.io/en/master/
fake = Faker()
fake.add_provider(company)

"""Functions for tasks to be used in the Tasl set"""

def get_id(pattern):
    #use scan on the key level 
    try:
        resp = requests.get(api_endpoint + 'keys?pattern=' + pattern, verify=False)
        r = resp.json()
        keys = r.get('examples')
        return keys
    except Exception as e:
        return {'error':str(e)}

fields = ['id','name','address','location']


""" Build the TaskSet """
class test(TaskSet):
    """ task functions to be used in the TaskSet """

    @tag('add_static_small_json')
    @task(3)
    def add_static_small_json(self):
        json_doc = json.dumps(smallObj)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=60,
            name='/api/v1/add_static_small_json')
        self.client.cookies.clear()


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
            timeout=60,
            name='/api/v1/add_random_small_json')
        self.client.cookies.clear()



    #POST nested JSON
    @tag('add_static_big_json')
    @task(3)
    def add_static_big_json(self):
        json_doc = json.dumps(bigObj)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=60,
            name='/api/v1/add_static_big_json')
        self.client.cookies.clear()


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
            timeout=60,
            name='/api/v1/add_random_big_json')
        self.client.cookies.clear()

    @tag('add_static_simple_json_hash')
    @task(3)
    def add_static_simple_json_hash(self):
        json_doc = json.dumps(smallObj)
        self.client.post('/api/v1/redisjson',
            data=json_doc,
            headers={'Content-Type': 'application/json'},
            timeout=60,
            name='/api/v1/add_static_simple_json_hash')
        self.client.cookies.clear()

    @tag('add_random_simple_json_hash')
    @task(3)
    def add_random_simple_json_hash(self):
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
            timeout=60,
            name='/api/v1/add_random_simple_json_hash')
        self.client.cookies.clear()

    @tag('getJSONByKey')
    #@task(3)
    def get_json_by_key(self):
        id = get_id('basicUser')
        self.client.get('/api/v1/doc/{}'.format(random.choice(id)), timeout=60, name='/api/v1/getJsonByKey')
        self.client.cookies.clear()


    @tag('getHashByKey')
    #@task(3)
    def get_hash_by_key(self):
        id = get_id('simpleHash')
        self.client.get('/api/v1/hash/{}'.format(random.choice(id)), timeout=60, name='/api/v1/getHashByKey')
        self.client.cookies.clear()


    @tag('getValueByKeyAndField')
    #@task(3)
    def get_json_by_key_and_field(self):
        id= get_id('basicUser')
        self.client.get('/api/v1/subdoc/{}/{}'.format(random.choice(id), random.choice(fields)), timeout=60, name='/api/v1/getValueByKeyAndFields')
        self.client.cookies.clear()

    @tag('getListOfFieldsByKey')
    #@task(1)
    def get_list_of_fields_by_key(self):
        id = get_id('advancedUser')
        self.client.get('/api/v1/fields/{}'.format(random.choice(id)), timeout=60, name='/api/v1/examples/getListOfFieldsByKey')
        self.client.cookies.clear()


    @tag('appendString')
    #@task(1)
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
            timeout=60,
            name='/api/v1/appendString')
        self.client.cookies.clear()


    @tag('NumIncrby')
    #@task(1)
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
            timeout=60,
            name='/api/v1/numbIncryBy')
        self.client.cookies.clear()

    @tag('NumMultiby')
    #@task(1)
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
            timeout=60,
            name='/api/v1/numMultiBy')
        self.client.cookies.clear()

""" Generate the load """

class GenerateLoad(HttpUser):
    tasks = [test]
    min_wait = 5000
    max_wait = 15000

