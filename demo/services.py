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
    print("DEBUG pattern {}".format(pattern))
    try:
        cur, keys  = rc.connection.scan(cursor=0,match=pattern+'*',count=cnt)
        result.extend(keys)
        # print("DEBUG scan_keys cur {}, keys {}; result {}".format(cur,keys, json.dumps(result)))
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
    id = str(uuid.uuid4())
    if 'id' not in kwargs.keys():
        key ='redisJSON:'+id
    else:
        key = kwargs['id']
    # print("DEBUG - ADD-JSON - key {} - json {}".format(key, json.dumps(kwargs)))
    try:
        rc.connection.jsonset(key, rc.Path.rootPath(), kwargs)
        return json.dumps(kwargs)
    except Exception as e:
        return {'error':str(e)}

def add_string(**kwargs):
    id = str(uuid.uuid4())
    key= "stringJSON:"+id
    try:
        rc.connection.set(key, json.dumps(kwargs))
        return json.dumps(kwargs)
    except Exception as e:
        return {'error':str(e)}
    
def get_string(key):
    try:
        return rc.connection.get(key)
    except Exception as e:
        return {'error': str(e)}


#Get a JSON value based on a key 
def getJsonByKey(key):
    try:
        return rc.connection.jsonget(key)
    except Exception as e:
        return {'error': str(e)}


def getArrayOfJsonSubByKey(key, field):
    try:
        return rc.connection.jsonmget(id, rc.Path('.'+field))
    except Exception as e:
        return {'error': str(e)}


def getSubdoc(id, field):
    try:
        ##rj.jsonget('obj', Path('.truth.coord'))
        return rc.connection.jsonget(id, rc.Path('.'+field))
    except Exception as e:
        return {'error': str(e)}


#Update a field on JSON at path. 
def updateField(key, field, str):
    try:
        rc.connection.jsonset(name=key, path='.'+field, obj=str, xx=True)
        return key
        # return rc.connection.jsonget(key)
    except Exception as e:
        return {'error': str(e)}


#Delete a whole JSON document: whole doc or by path
def deleteAJson(key):
    try: 
        rc.connection.jsondel(name=key)
        return key
    except Exception as e:
        return {'error': str(e)}

#Delete a whole JSON document: whole doc or by path
def deleteAPathInJson (key,field):
    try: 
        rc.connection.jsondel(name=key, path='.'+field)
        return key
    except Exception as e:
        return {'error': str(e)}


#Append the json-string value(s) the string at path .
def appendStringToField(key, field, str):
    try:
        #restrict to the selected fields 
        #id, field, value
        # print('appendStringToField: key {}, field {}, str {} '.format(key,field,str))
        rc.connection.jsonstrappend(name=key, path='.'+ field, string=str)
        return rc.connection.jsonget(key)
    except Exception as e:
        return {'error': str(e)}


#Add an array of JSON
#def jsonarrappend(self, name, path='.', *args)
def addArrayOfJSON(key, field,**arr):
    try:
        print('appendArrayToField: key {}, field {}, arr {} '.format(key,field,arr))
        rc.connection.jsonarrappend(key, '.'+field, arr)
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


### Add JSON through HASH: ###
def addjson_hash(**kwargs):
    #create a python obj(dict) first
    id = str(uuid.uuid4())
    if 'id' not in kwargs.keys():
        key ='hash:'+id
    else:
        key = kwargs['id']
    try:
        rc.connection.hmset(key,kwargs)
        return json.dumps(kwargs)
    except Exception as e:
        return {'error-multiBy': str(e)}


def getjson_hash_field(key,field):
    try:
        return rc.connection.hget(key,field)
    except Exception as e:
        return {'error-multiBy': str(e)}

def getjson_hash(key):
    try:
        return rc.connection.hgetall(key)
    except Exception as e:
        return {'error-multiBy': str(e)}


#Update a field on JSON at path. 
def updateField_hash(key, field, str):
    try:
        rc.connection.hset(key, field, str)
        return rc.connection.hgetall(key)
    except Exception as e:
        return {'error': str(e)}

