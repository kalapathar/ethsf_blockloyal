from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
import subprocess
from subprocess import Popen, PIPE
import re
from string import printable
import requests
import json
import time

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {'hello': 'world'}

@app.route("/")
def main():
    return "Hello World!"

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)