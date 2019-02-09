# coding:utf-8
import json
from flask import Flask, jsonify, make_response, request, Response

app = Flask(__name__)

@app.route('/api/<name>', methods=['GET'])
def get_json(name):
  NAME = name
  result = {
    "data": {
      "id": 1,
      "name": NAME
      }
    }
  return jsonify(result) 

if __name__ == "__main__":
  app.run()