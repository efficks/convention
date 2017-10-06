#!/usr/bin/env python

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")
app.config.from_pyfile('config.cfg')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(port=8081)
