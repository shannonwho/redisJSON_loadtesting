# If to pre-load some data from the local file
# from dataload import load_data

import json
import string
import app
import uuid
from utils import redis_client as rc
from itertools import zip_longest #scan keys in batches
import uuid


examples_reference = {
    'index': 'examples_idx',
    'index_name_delimiter': ':',
    'fields': 'id,_id,number,name,age,description,address,location,latitude,longitude,zipcode,home,city,country,addressLn,activeStatus,sclr,str,sub_doc,array_of_docs'
}


def scan_keys(pattern,cnt):
    "Returns a list of all the keys matching a given pattern"
    result = []
    try:
        cur, keys  = rc.connection.scan(cursor=0, match=pattern+'*',count=cnt)
        result.extend(keys)
        # Get all keys Use below code
        # while cur != 0:
        #     cur, keys = rc.connection.scan(cursor=cur, match=pattern+'*',count=10)
        #     result.extend(keys)
        print("DEBUG scan_keys {}".format(json.dumps(result)))
        return result
    except Exception as e:
        return {'error':str(e)}


def scan_fields(key, p):
    '''Returns the key names in the dictionary JSON value under path at key name'''
    try:
        return rc.connection.jsonobjkeys(key, path=p)
    except Exception as e:
        return {'error':str(e)}


def add_json(**kwargs):
    #restrict to the selected fields 
    # allowed_fields = examples_reference['fields'].split(',')
    #create a python obj(dict) first
    new_obj = {}
    id_template = 'simple:' + str(uuid.uuid4())
    for key,value in kwargs.items():
        # if key in allowed_fields:
            new_obj[key] = value
            
    id = new_obj['id'] if new_obj['id'] else id_template
    
    print('DEBUG SERVICE {}'.format(json.dumps(new_obj)))

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


#Append the json-string value(s) the string at path .
def appendStringToField(key, field, str):
    try:
        #restrict to the selected fields 
        #id, field, value
        print('appendStringToField: key {}, field {}, str {} '.format(key,field,str))
        rc.connection.jsonstrappend(name=key, path='.'+ field, string=str)
        return rc.connection.jsonget(key)
    except Exception as e:
        return {'error': str(e)}


#Add an array of JSON
def addArrayOfJSON(len,**kwargs):
    try:
        rc.connection.jsonarrappend()
    except Exception as e:
        return {'error':str(e)}


#Increase the numeric JSON value under path at key with the provided number
def numIncrBy(key, field, incrby):
    try:
        rc.connection.jsonnumincrby(key, path='.'+field, number=incrby)
        return rc.connection.jsonget(key)
    except Exception as e:
        return {'error-numIncrBy': str(e)}


# Multiplies the numeric JSON value udner path at key with the provided number 
def numMultiBy(key, field, multiby):
    try:
        rc.connection.jsonnummultby(key, path='.'+field, number=multiby)
        return rc.connection.jsonget(key)
    except Exception as e:
        return {'error-multiBy':str(e)}


# Add JSON through HASH:
def addjson_hash(**kwargs):
    #restrict to the selected fields 
    allowed_fields = examples_reference['fields'].split(',')
    #create a python obj(dict) first
    new_obj = {}
    id_template = 'simpleHash:' + str(uuid.uuid4())

    for key,value in kwargs.items():
        # if key in allowed_fields:
            new_obj[key] = value
    id = new_obj['id'] if new_obj['id'] else id_template
    try:
        rc.connection.hmset(id,kwargs)
        return rc.connection.hgetall(id)
    except Exception as e:
        return {'error-multiBy': str(e)}

def getjson_hash(key):
    try:
        return rc.connection.hgetall(id)
    except Exception as e:
        return {'error-multiBy': str(e)}


