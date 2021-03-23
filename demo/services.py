# If to pre-load some data from the local file
# from dataload import load_data

import json
import string
import app
import uuid
from utils import redis_client as rc
from itertools import zip_longest #scan keys in batches


examples_reference = {
    'index': 'examples_idx',
    'index_name_delimiter': ':',
    'fields': '_id,name,description,address,location,latitude,longitude,zipcode,home,city,country,addressLn,business'
}

# obj = {
#     '_id': 42,
#     'name': 'Shannon',
#     'zipcode': 123456,
#     'address': ['home address', 'business address'],
#     'location':{
#         'latitude':33.685909,
#         'longitude':-117.824722
#     }
# }

def scan_keys(pattern,cnt):
    "Returns a list of all the keys matching a given pattern"
    result = []
    try:
        cur, keys  = rc.connection.scan(cursor=0, match=pattern+'*',count=10)
        result.extend(keys)
        # Get all keys Use below code
        # while cur != 0:
        #     cur, keys = rc.connection.scan(cursor=cur, match=pattern+'*',count=10)
        #     result.extend(keys)
        return result
    except Exception as e:
        return {'error':str(e)}


def scan_fields(key, path):
    "Return the keys in the object that's referenced by path"
    try:
        return rc.connection.jsonobjkeys(key,rc.Path.rootPath())
    except Exception as e:
        return {'error':str(e)}


def add_json(**kwargs):
    #restrict to the selected fields 
    allowed_fields = examples_reference['fields'].split(',')
    #create a python obj(dict) first
    new_obj = {}
    id = "Topshot:" + str(uuid.uuid4())
    for key,value in kwargs.items():
        if key in allowed_fields:
            new_obj[key] = value
    new_obj['_id'] = id

    try:
        rc.connection.jsonset(id, rc.Path.rootPath(), new_obj)
        return rc.connection.jsonget(id)

    except Exception as e:
        return {'error':str(e)}

#Get a JSON value based on a key 
def getJsonByKey(key):
    try:
        return rc.connection.jsonget(key)
    except Exception as e:
        return {'error': str(e)}


#Add an array of JSON
def addArrayOfJSON(len,**kwargs):
    try:
        rc.connection.jsonarrappend()
    except Exception as e:
        return {'error':str(e)}


def getArrayOfJsonSubByKey(key, field):
    try:
        # json.mget Topshot:4209e7d8-5167-49a7-a00a-f88291b40a24 Topshot:2b5c6883-8126-4b0d-8ddf-8a7fe723b967 .name
        return rc.connection.jsonmget(id, rc.Path('.'+field))
    except Exception as e:
        return {'error': str(e)}


def getSubdoc(id, field):
    try:
        ##rj.jsonget('obj', Path('.truth.coord'))
        return rc.connection.jsonget(id, rc.Path('.'+field))
    except Exception as e:
        return {'error': str(e)}


def get_examples(limit=10,offset=0):
    try:
        just_ids = []
        name_and_ids = rc.connection.zrange(examples_reference['index'], offset, limit)
        for i in range(len(name_and_ids)):
            just_ids.append(name_and_ids[i].split(':', 1)[1])
        return just_ids
    except Exception as e:
        app.logger.error(e)
        return {'error': str(e)}

# def get_examples_by_name(name, limit=10,offset=0):
#     lex_min = '{}{}'.format('[', name)
#     lex_max = '{}{}'.format(lex_min, str(b'\xff', 'iso-8859-1'))
#     try:
#         name_id_pairs = []
#         name_and_ids = redis_client.connection.zrangebylex(examples_reference['index'], lex_min, lex_max, offset, limit)
#         for i in range(len(name_and_ids)):
#             match = name_and_ids[i].split(':', 1)
#             name_id_pairs.append({'name': match[0], 'id': match[1]})
#         return name_id_pairs
#     except Exception as e:
#         app.logger.error(e)
#         return {'error': str(e)}





