from locust import HttpUser, User, TaskSet, task, web, runners, between, tag
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

def get_id():
    #use scan on the key level 
    try:
        resp = requests.get(api_endpoint + 'examples', verify=False)
        r = resp.json()
        keys = r.get('examples')
        return keys
    except Exception as e:
        return {'error':str(e)}


""" Build the TaskSet """
class test(TaskSet):
    """ task functions to be used in the TaskSet """
    # @task
    # def on_start(self):
    #     self.client.get("/examples", verify=True)    
 
    # POST simple JSON 
 
    @tag('addSimpleJSON')
    @task (2)
    def add_simple_json(self):
        simple_json = {
            'name': fake.company(),
            'geo': fake.coordinate(),
            'number': fake.random_int(),
            'description': fake.bs()
        }

        self.client.post('/api/v1/examples',
            json=simple_json,
            headers={'Content-Type': 'application/json'},
            timeout=20,
            name='/api/v1/simple_json')
        self.client.cookies.clear()

    #POST nested JSON

    @tag('addNestedJSON')
    @task(1)
    def add_nested_json(self):
        nested_json = {
            'name': fake.company(),
            'description': fake.bs(),
            'location':{
                'latitude': fake.latitude(),
                'longitude':fake.longitude()
                },
            'address': [fake.street_address(), fake.street_address()]
            }
        self.client.post('/api/v1/examples',
            data=json.dumps(nested_json,use_decimal=True),
            headers={'Content-Type': 'application/json'},
            timeout=20,
            name='/api/v1/nested_json')
        self.client.cookies.clear()

    @tag('getJSONByKey')
    @task(3)
    def get_json_by_key(self):
        id = get_id()
        self.client.get('/api/v1/examples/{}'.format(random.choice(id)), timeout=20, name='/api/v1/examples/getJsonByKey')
        self.client.cookies.clear()

    @tag('getJSONByKeyAndField')
    @task(3)
    def get_json_by_key_and_field(self):
        id= get_id()
        self.client.get('/api/v1/examples/{}/description'.format(random.choice(id)), timeout=20, name='/api/v1/examples/getJsonByKeyAndFields')
        self.client.cookies.clear()


""" Generate the load """

class GenerateLoad(HttpUser):
    tasks = [test]
    min_wait = 5000
    max_wait = 15000

