#!/usr/bin/env python

from flask import Flask, send_from_directory
from flask_restful import Api
from models import Convention

app = Flask(__name__, static_folder="static")
app.config.from_pyfile('config.cfg')
api = Api(app)
api.add_resource(Convention, '/api/convention')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(port=8081)
