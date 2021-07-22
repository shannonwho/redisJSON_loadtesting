import logging
from flask import Flask, request, render_template, Response
import requests

import config
import json
import random
import services

app = Flask(__name__)
app.config['ENV'] = config.ENV
app.config['REDIS_HOST'] = config.REDIS_HOST
app.config['REDIS_PORT'] = config.REDIS_PORT
app.app_context().push()


#set log level based on environment
if app.config['ENV'] == 'development':
    app.logger.setLevel(logging.DEBUG)
    app.config['DEBUG'] = True
    app.logger.debug('Environment is development setting loglevel and debug mode.')
    app.logger.debug('LogLevel: debug')
else:
    app.logger.setLevel(logging.INFO)
    app.logger.debug('LogLevel: info')

#log out things being set specifically
app.logger.debug('DEBUG: {}'.format(str(app.config['DEBUG'])))
app.logger.debug('ENV: {}'.format(app.config['ENV']))
app.logger.debug('REDIS_HOST: {}'.format(app.config['REDIS_HOST']))
app.logger.debug('REDIS_PORT: {}'.format(app.config['REDIS_PORT']))


""" 
VIEWS
Each view path pulls from it's associated template.  The main.html is a parent template 
Javascript files are associated by naming convention: home.html --> home.js
"""

# Test a basic page route here: 
@app.route('/', methods=['GET'])
def viewHome():
    # app.logger.info(
    #     'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    return render_template('home.html', environment=app.config['ENV'])

# Test basic example page: 
@app.route('/examples', methods=['GET'])
def viewExamples():
    return render_template('examples.html')

"""
API using RedisJSON
- GET
"""


# get a list of keys that's store with RedisJSON with the key pattern
@app.route('/api/v1/keys', methods=['GET'])
def api_get_keys():
    limit = request.args.get('limit') if request.args.get('limit') else 10
    pattern = request.args.get('pattern') if request.args.get('pattern') else 'basicUser'
    app.logger.info(
        'limit: %s  pattern: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    #show all the json item 
    keys = services.scan_keys(pattern,cnt=limit)
    full_json = []
    for k in keys:
        full_json.append(services.getJsonByKey(k))

    try:
        if 'error' not in keys:
            return Response(json.dumps({'status': 'ok', 'json': keys}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': keys}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)

#get a JSON document by its key 
@app.route('/api/v1/doc/<id>', methods=['GET'])
def api_get_example(id):
    # app.logger.info(
    #     'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    #Get JSON document by ID
    json_doc = services.getJsonByKey(id)
    try:
        return Response(json.dumps({'status':'ok', 'json': json_doc}, indent=4, default=str),
                            mimetype='application/json', status=200)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


# # get a list of keys that's store with RedisJSON 
# @app.route('/api/v1/fields/<id>', methods=['GET'])
# def api_get_fields(id):
#     path = request.args.get('path') if request.args.get('path') else '.'
#     #show all the fields of a key with the path
#     fields = services.scan_fields(id,path)
#     try:
#         return Response(json.dumps({'status': 'ok', 'examples': fields}, indent=4, default=str),
#                         mimetype='application/json', status=200)
#     except Exception:
#         app.logger.warn('request failed:', exc_info=True)
#         return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
#                         status=400)


#get a subdocument of a JSON document
@app.route('/api/v1/subdoc/<id>/<field>', methods=['GET'])
def api_get_subdoc(id,field):
    #Get JSON document by ID
    json_doc = services.getSubdoc(id,field)
    try:
        return Response(json.dumps({'status':'ok', 'json': json_doc}, indent=4, default=str),
                            mimetype='application/json', status=200)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


"""
API using RedisJSON
- POST
"""


#Use RedisJSON for adding a new JSON 
@app.route('/api/v1/redisjson', methods=['POST'])
def api_add_example():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    data = request.get_json(force=True)
    add_json = services.add_json(**data)

    try:
        if 'error' not in add_json:
            return Response(json.dumps({'status': 'ok', 'json': add_json}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': "add_json"}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)



"""
API using RedisJSON
- PUT
"""

#Update a single field of JSON 
@app.route('/api/v1/redisjson/update', methods=['PUT'])
def api_update_field():
    data = request.get_json(force=True)

    if data:
        key = data.get('key', None)
        field = data.get('field', None)
        str = data.get('str', None)
        #call numIncrBy function
        updateStr = services.updateField(key,field,str)
    else:
        result = {'error': 'invalid request'}

    try:
        if 'error' not in data:
            return Response(json.dumps({'status':'ok', 'json': updateStr}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': updateStr}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


"""
API using RedisJSON
- DELETE
"""
#Delete a whole JSON (whole doc or by path) 
@app.route('/api/v1/redisjson/delete/<id>', methods=['DELETE'])
def api_delete_field(id):
    json_doc = services.deleteAJson(id)
    try:
        return Response(json.dumps({'status':'ok', 'json': json_doc}, indent=4, default=str),
                            mimetype='application/json', status=200)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)

#Append a string value to a field
@app.route('/api/v1/redisjson/append', methods=['PUT'])
def api_append_field():
    app.logger.info(
        'APPEND: method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    
    data = request.get_json(force=True)
    if data:
        key = data.get('key', None)
        field = data.get('field', None)
        str = data.get('str', None)
        #call numIncrBy function
        appenStr = services.appendStringToField(key,field,str)
    else:
        result = {'error': 'invalid request'}

    try:
        if 'error' not in data:
            return Response(json.dumps({'status':'ok', 'json': appenStr}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': appenStr}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


#Append an array to a field
@app.route('/api/v1/redisjson/appendarray', methods=['PUT'])
def api_append_array():
    app.logger.info(
        'APPEND-ARRAY: method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    
    data = request.get_json(force=True)
    if data:
        key = data.get('key', None)
        field = data.get('field', None)
        arr = data.get('arr', None)
        #call numIncrBy function
        appenArray = services.addArrayOfJSON(key,field,**arr)
    else:
        result = {'error': 'invalid request'}

    try:
        if 'error' not in data:
            return Response(json.dumps({'status':'ok', 'json': appenArray}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': appenArray}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


#Increase a numeric field in a JSON
@app.route('/api/v1/redisjson/increby', methods=['PUT'])
def api_num_incrby():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    data = request.get_json(force=True)
    if data:
        key = data.get('key', None)
        field = data.get('field', None)
        num = data.get('num', None)
        #call numIncrBy function
        incrData = services.numIncrBy(key, field, num)
        app.logger.info("PUT! {} and {}".format(field, num))
    else:
        result = {'error': 'invalid request'}
    
    try:
        if 'error' not in incrData:
            return Response(json.dumps({'status': 'ok', 'json': incrData}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': "incrData"}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)



#Increase a numeric field in a JSON
@app.route('/api/v1/redisjson/multiby', methods=['PUT'])
def api_num_multiby():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    data = request.get_json(force=True)
    if data:
        key = data.get('key', None)
        field = data.get('field', None)
        num = data.get('num', None)
        #call numIncrBy function
        multiData = services.numMultiBy(key, field, num)

    else:
        result = {'error': 'invalid request'}
    
    try:
        if 'error' not in multiData:
            return Response(json.dumps({'status': 'ok', 'json': multiData}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': "multiData"}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


"""
API using Redis's Hash data structure
"""

#Use Redis's Hash for adding a new JSON 
@app.route('/api/v1/hash', methods=['POST'])
def api_add_example_hash():
    app.logger.info('method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    data = request.get_json(force=True)
    add_json_hash = services.addjson_hash(**data)
    # app.logger.info('add_json_hash{}'.format(data))
    try:
        if 'error' not in add_json_hash:
            return Response(json.dumps({'status': 'ok', 'json': add_json_hash}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': "add_json"}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


# Use Redis's Hash for getting the JSON document 
@app.route('/api/v1/hash/<id>', methods=['GET'])
def api_get_example_hash(id):
    # app.logger.info('method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    #show all the json item 
    json_doc = services.getjson_hash(id)

    try:
        if 'error' not in json_doc:
            return Response(json.dumps({'status':'ok', 'json': json_doc}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': json_doc}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)

#first layer only
@app.route('/api/v1/hash/<id>/<field>', methods=['GET'])
def api_get_hash_field(id,field):
    # app.logger.info('method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    #show all the json item 
    fieldValue = services.getjson_hash_field(id,field)

    try:
        if 'error' not in fieldValue:
            return Response(json.dumps({'status':'ok', 'json': fieldValue}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': fieldValue}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)



#Update a single field of JSON 
@app.route('/api/v1/hash/update', methods=['PUT'])
def api_update_field_hash():
    data = request.get_json(force=True)

    if data:
        key = data.get('key', None)
        field = data.get('field', None)
        str = data.get('str', None)
        #call numIncrBy function
        updateStr = services.updateField_hash(key,field,str)
    else:
        result = {'error': 'invalid request'}

    try:
        if 'error' not in data:
            return Response(json.dumps({'status':'ok', 'json': updateStr}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': updateStr}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


"""
API using Redis String
"""

@app.route('/api/v1/string', methods=['POST'])
def api_post_string():
    data = request.get_json(force=True)
    # app.logger.info('POST - String - data {}'.format(json.dumps(data)))

    add_json_string = services.add_string(**data)

    try:
        if 'error' not in add_json_string:
            return Response(json.dumps({'status': 'ok', 'json': add_json_string}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': "add_json"}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


@app.route('/api/v1/string/<id>', methods=['GET'])
def api_get_string(id):
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    #show all the json item 
    json_doc = services.get_string(id)

    try:
        if 'error' not in json_doc:
            return Response(json.dumps({'status':'ok', 'json': json_doc}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': json_doc}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)

#first layer only
@app.route('/api/v1/string/<id>/<field>', methods=['GET'])
def api_get_nested_string(id,field):
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    #show all the json item 
    json_string = services.get_string(id)
    #one layer for now
    #deserialized JSON String
    json_object = json.loads(json_string)
    #update a field on deserialized JSON
    if json_object:
        json_doc = json_object[field]
    else:
        json_doc = {'error': 'invalid request'}

    try:
        if 'error' not in json_doc:
            return Response(json.dumps({'status':'ok', 'json': json_doc}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': json_doc}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


@app.route('/api/v1/string/update', methods=['PUT'])
def api_put_string():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    # parse PUT request
    data = request.get_json(force=True)

    if data:
        key = data.get('key', None)
        field = data.get('field', None)
        str = data.get('str', None)
        #call numIncrBy function
        
        json_string = services.get_string(key)
        #deserialized JSON String
        json_object = json.loads(json_string)
        #update a field on deserialized JSON
        json_object[field] = str
        #replace the old json string
        json_set = services.add_string(**json_object)

    else:
        result = {'error': 'invalid request'}

    try:
        if 'error' not in json_set:
            return Response(json.dumps({'status':'ok', 'json': json_set}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': json_set}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)







#Update a field in json doc on HASH

if __name__ == '__main__':
#    bootstrap.init_app(app)
#    nav.init_app(app)
   app.debug = True
   app.run(port=5000, host="0.0.0.0")
