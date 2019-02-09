# coding:utf-8
import json
from flask import Flask, jsonify, make_response, request, Response
from flask_api import status

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post_json():
  try:
    json = request.get_json()  # Get POST JSON
    NAME = json['name']
    result = {
      "data": {
        "id": 1,
        "name": NAME
        }
      }
    return jsonify(result) 
  except Exception as e:
    result = error_handler(e)
    return result

@app.errorhandler(400)
@app.errorhandler(404)
@app.errorhandler(500)
def error_handler(error):
    response = jsonify({ 
                          "error": {
                          "type": error.name, 
                          "message": error.description 
                          }
                      })
    return response, error.code

if __name__ == "__main__":
  app.debug=True
  app.run()