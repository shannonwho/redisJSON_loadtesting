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
#,'location','latitude','longitude' 

""" Build the TaskSet """
class test(TaskSet):
    """ task functions to be used in the TaskSet """
    # @task
    # def on_start(self):
    #     self.client.get("/examples", verify=True)    
 
    # POST simple JSON 
 
    @tag('addSimpleJSON')
    @task (1)
    def add_simple_json(self):
        simple_json = {
            'id':   "simple:" + str(uuid.uuid4()),
            'name': fake.company(),
            'number': fake.random_int(min=0, max=15),
            'location': str(fake.latitude()),
            'address': fake.street_address()
        }
        simple_json_d = json.dumps(simple_json)

        self.client.post('/api/v1/examples',
            data=simple_json_d,
            headers={'Content-Type': 'application/json'},
            timeout=20,
            name='/api/v1/simple_json')
        self.client.cookies.clear()

    #POST nested JSON

    # @tag('addNestedJSON')
    # @task(1)
    # def add_nested_json(self):
    #     nested_json = {
    #         'id': "nested:" + str(uuid.uuid4()),
    #         'name': fake.company(),
    #         'number': str(fake.random_int(min=0, max=15)),
    #         'location':{
    #             'latitude': fake.latitude(),
    #             'longitude':fake.longitude(),
    #             'number': fake.random_int(min=0, max=15)
    #             },
    #         'address': [fake.street_address(), fake.street_address(), fake.street_address()]
    #         }
    #     self.client.post('/api/v1/examples',
    #         data=json.dumps(nested_json,use_decimal=True),
    #         headers={'Content-Type': 'application/json'},
    #         timeout=20,
    #         name='/api/v1/nested_json')
    #     self.client.cookies.clear()

    # @tag('getJSONByKey')
    # @task(3)
    # def get_json_by_key(self):
    #     id = get_id('simple')
    #     self.client.get('/api/v1/examples/{}'.format(random.choice(id)), timeout=20, name='/api/v1/examples/getJsonByKey')
    #     self.client.cookies.clear()

    # @tag('getValueByKeyAndField')
    # @task(3)
    # def get_json_by_key_and_field(self):
    #     id= get_id('simple')
    #     self.client.get('/api/v1/examples/{}/{}'.format(random.choice(id), random.choice(fields)), timeout=20, name='/api/v1/examples/getValueByKeyAndFields')
    #     self.client.cookies.clear()

    # @tag('getListOfFieldsByKey')
    # @task(1)
    # def get_list_of_fields_by_key(self):
    #     id = get_id('nested')
    #     self.client.get('/api/v1/fields/{}'.format(random.choice(id)), timeout=20, name='/api/v1/examples/getListOfFieldsByKey')
    #     self.client.cookies.clear()


    # @tag('addNewStringToJSONField')
    # @task(1)
    # def add_new_string_to_a_field(self):
    #     id = get_id('simple')
    #     append = {
    #         'id': id,
    #         'field': random.choice(fields),
    #         'value': fake.company()
    #     }

    #     self.client.post('/api/v1/append',
    #         data=json.dumps(append),
    #         headers={'Content-Type': 'application/json'},
    #         timeout=20,
    #         name='/api/v1/addNewStringToJSONField')
    #     self.client.cookies.clear()

    @tag('NumIncrby')
    @task(1)
    def num_incr_by(self):
        id = get_id('simple')
        fieldNum = {
            'key': random.choice(id),
            'field': 'number',
            'num': random.randint(1,10)
        }
        self.client.put('/api/v1/examples/increby',
            data=json.dumps(fieldNum),
            headers={'Content-Type': 'application/json'},
            timeout=20,
            name='/api/v1/numbIncryBy')
        self.client.cookies.clear()

    @tag('NumMultiby')
    @task(1)
    def num_multi_by(self):
        id = get_id('simple')
        fieldNum = {
            'key': random.choice(id),
            'field': 'number',
            'num': random.randint(1,10)
        }
        self.client.put('/api/v1/examples/multiby',
            data=json.dumps(fieldNum),
            headers={'Content-Type': 'application/json'},
            timeout=20,
            name='/api/v1/numMultiBy')
        self.client.cookies.clear()

""" Generate the load """

class GenerateLoad(HttpUser):
    tasks = [test]
    min_wait = 5000
    max_wait = 15000

