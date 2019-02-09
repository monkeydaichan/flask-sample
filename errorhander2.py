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
    result = errorhandling(e)
    return result, status.HTTP_500_INTERNAL_SERVER_ERROR

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

def errorhandling(error):
  exception_type = error.__class__.__name__
  exception_message = str(error)
  result_error = { 
                    "error": { 
                      "type": exception_type, 
                      "message": exception_message 
                    }
                  }
  return make_response(jsonify(result_error))

if __name__ == "__main__":
  app.debug=True
  app.run()