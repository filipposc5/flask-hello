import os
from flask import Flask
from flask import json
app = Flask(__name__)

node = os.uname()[1]

with open( os.path.join(os.path.dirname(__file__), 'config.json') ) as f:
    appconfig = json.loads(f.read())


@app.route('/')
def hello_world():
    return 'Hello World! //{0}'.format(node)

if __name__ == '__main__':
    app.run(port = int(appconfig['port']))

