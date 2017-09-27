import json
from random import SystemRandom as Random
try:    jokes = json.load(open('jn.json'))
except: jokes = {'value': ['Error opening database']}

def application(environment, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    Random().shuffle(jokes['value'])
    return jokes['value'][0]
