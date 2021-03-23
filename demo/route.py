import json
from flask import request, render_template, Response
import services
import app

""" VIEWS
Each view path pulls from it's associated template.  The main.html is a parent template 

Javascript files are associated by naming convention: home.html --> home.js
"""

@app.route('/', methods=['GET'])
def viewHome():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    app.logger.debug('before render')
    return render_template('home.html', environment=app.config['ENV'])

@app.route('/examples', methods=['GET'])
def viewExamples():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    full_examples = []
    examples = services.get_examples(limit=11, offset=0)
    app.logger.debug(examples)
    if 'error' in examples:
        examples = []
    if examples is None:
        examples = []
    for i in range(len(examples)):
        full_examples.append(services.get_example(examples[i]))
    return render_template('examples.html', examples=full_examples)


"""
APIS
"""
@app.route('/api/v1/examples', methods=['GET'])
def api_get_examples():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    if request.args.get('limit'):
        limit = 10 if request.args.get('limit') == 0 else request.args.get('limit')
    else:
        limit = 10
    offset = request.args.get('offset') if request.args.get('offset') else 0

    examples = services.get_examples(limit, offset)
    try:
        if 'error' not in examples:
            return Response(json.dumps({'status': 'ok', 'examples': examples}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': examples}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)

@app.route('/api/v1/examples/<id>', methods=['GET'])
def api_get_exampl(id):
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    example = services.get_example(id)
    try:
        if 'error' not in example:
            return Response(json.dumps({'status':'ok', 'example': example}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': example}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)

@app.route('/api/v1/examples/name/<name>', methods=['GET'])
def get_examples_using_name(name):
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    if request.args.get('limit'):
        limit = 10 if request.args.get('limit') == 0 else request.args.get('limit')
    else:
        limit = 10
    offset = request.args.get('offset') if request.args.get('offset') else 0

    examples = services.get_examples_by_name(name, limit, offset)
    try:
        if 'error' not in examples:
            return Response(json.dumps({'status': 'ok', 'examples': examples}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': examples}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)


@app.route('/api/v1/examples', methods=['POST'])
def api_add_example():
    app.logger.info(
        'method: %s  path: %s  query_string: %s' % (request.method, request.path, request.query_string.decode('UTF-8')))
    data = request.get_json(force=True)
    app.logger.debug('request body: {}'.format(data))
    add_example = services.add_example(**data)
    try:
        if 'error' not in add_example:
            return Response(json.dumps({'status': 'ok', 'examples': add_example}, indent=4, default=str),
                            mimetype='application/json', status=200)
        else:
            return Response(json.dumps({'error': examples}, indent=4, default=str), mimetype='application/json',
                            status=400)
    except Exception:
        app.logger.warn('request failed:', exc_info=True)
        return Response(json.dumps({'error': 'Attribute Error'}, indent=4, default=str), mimetype='application/json',
                        status=400)
