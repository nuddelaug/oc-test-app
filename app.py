import json
from random import SystemRandom as Random
from flask import Flask, jsonify, request
from flask_autodoc.autodoc import Autodoc
import os
try:    jokes = json.load(open('jn.json'))
except: jokes = {'value': ['Error opening database']}

app = Flask(__name__)
app.secret_key = os.urandom(24)
auto = Autodoc(app)

@app.route('/health/', methods=['GET'])
@auto.doc()
def health():
    """Health check entrypoint"""
    jl = len(jokes.get('value'))
    if jl > 1:
        return jsonify(dict(status='ok', message='%s entries in joke book' % jl))
    # fail if not true

@app.route('/', methods=['GET'])
def documentation():
    """Documentation access"""
    return auto.html(
                     title='API endpoint documentation',
                     author='Michael Lang <Michael.Lang@ctbto.org>',)

@app.route('/joke/random/', methods=['GET', 'POST'])
@auto.doc()
def get_joke():
    Random().shuffle(jokes.get('value'))
    jl = len(jokes.get('value'))
    if request.method == 'GET':
        return jsonify(dict(status='ok', joke=jokes.get('value')[0]))
    elif request.method == 'POST':
        limit = int(request.args.get('limit', 1))
        category = request.args.get('category', False)
        if limit > jl:  limit = jl
        if category == False:
            return jsonify(dict(status='ok', joke=jokes.get('value')[:limit]))
        content = filter(lambda x: category in x['categories'], jokes.get('value'))
        if limit > len(content):    limit = len(content)
        return jsonify(dict(status='ok', joke=content[:limit]))

if __name__ == '__main__':
    app.debug = False
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)
