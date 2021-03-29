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
added this to make sure there is no other caching happening (was during a debug session may not be needed)
"""
@app.after_request
def set_response_headers(response):
    if request.path.startswith('/api/'):
        app.logger.debug('API request remove cache headers')
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response

""" 
VIEWS
Each view path pulls from it's associated template.  The main.html is a parent template 
Javascript files are associated by naming convention: home.html --> home.js
"""

# Test a basic page route here: 
@app.route('/', methods=['GET'])
def viewHome():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    app.logger.debug('before render')
    return render_template('home.html', environment=app.config['ENV'])

# Test basic example page: 
@app.route('/examples', methods=['GET'])
def viewExamples():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    full_json = []
    keys = services.scan_keys("Topshot*", cnt=10)

    app.logger.debug(keys)
    if 'error' in keys:
        keys = []
    if keys is None:
        keys = []
    for i in range(len(keys)):
        full_json.append(services.getJsonByKey(keys[i]))
    return render_template('examples.html', keys= keys, examples=full_json)

"""
API using RedisJSON
"""
# get a list of keys that's store with RedisJSON with the key pattern
@app.route('/api/v1/keys', methods=['GET'])
def api_get_keys():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    if request.args.get('limit'):
        limit = 10 if request.args.get('limit') == 0 else request.args.get('limit')
    else:
        limit = 10
    # offset = request.args.get('offset') if request.args.get('offset') else 0
    pattern = request.args.get('pattern') if request.args.get('pattern') else 'simple'

    #show all the json item 
    keys = services.scan_keys(pattern,cnt=limit)
    full_json = []
    for k in keys:
        full_json.append(services.getJsonByKey(k))

    # examples = services.get_examples(limit, offset)
    try:
        if 'error' not in keys:
            return Response(json.dumps({'status': 'ok', 'examples': keys}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': keys}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


# get a list of keys that's store with RedisJSON 
@app.route('/api/v1/fields/<id>', methods=['GET'])
def api_get_fields(id):
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    path = request.args.get('path') if request.args.get('path') else '.'

    
    #show all the fields of a key with the path
    fields = services.scan_fields(id,path)

    try:
        if 'error' not in fields:
            return Response(json.dumps({'status': 'ok', 'examples': fields}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': fields}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


#get a JSON document by its ID
@app.route('/api/v1/examples/<id>', methods=['GET'])
def api_get_example(id):
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    #Get JSON document by ID
    json_doc = services.getJsonByKey(id)

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


#get a subdocument of a JSON document
@app.route('/api/v1/examples/<id>/<field>', methods=['GET'])
def api_get_subdoc(id,field):
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    #Get JSON document by ID
    json_doc = services.getSubdoc(id,field)
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


#get a list of attributes on a JSON by a list of keys (mget)

# @app.route('/api/v1/append', methods=['POST'])
# def manipute_json_field():
#     app.logger.info(
#         'APPEND: method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    
#     data = request.get_json(force=True)
#     app.logger.debug('APPEND request body: {}'.format(data))

    # keyname =  request.args.get('keyname') if request.args.get('keyname') else 'simple'

    # json_doc = services.appendStringToField(**data)

    # try:
    #     if 'error' not in json_doc:
    #         return Response(json.dumps({'status':'ok', 'json': json_doc}, indent=4, default=str),
    #                         mimetype='application/json', status=200)
    #     else:
    #         return Response(json.dumps({'error': json_doc}, indent=4, default=str), mimetype='application/json',
    #                         status=400)
    # except Exception:
    #     app.logger.warn('request failed:', exc_info=True)
    #     return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
    #                     status=400)



#Incrememt an numeric field in JSON 
"""
 rj.jsonset('num', Path.rootPath(), 1)
        self.assertEqual(2, rj.jsonnumincrby('num', Path.rootPath(), 1))
        self.assertEqual(2.5, rj.jsonnumincrby('num', Path.rootPath(), 0.5))
        self.assertEqual(1.25, rj.jsonnumincrby('num', Path.rootPath(), -1.25))
"""



#Use RedisJSON for adding example 
@app.route('/api/v1/examples', methods=['POST'])
def api_add_example():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    data = request.get_json(force=True)
    app.logger.debug('request body: {}'.format(data))

    # keyname =  request.args.get('keyname') if request.args.get('keyname') else 'simple'

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


if __name__ == '__main__':
#    bootstrap.init_app(app)
#    nav.init_app(app)
   app.debug = True
   app.run(port=5000, host="0.0.0.0")
