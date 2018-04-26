from flask import Flask, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def create():
   data = request.get_json(force=True)
   try:
       value = int(data['value'])
   except (KeyError, TypeError, ValueError):
       raise JsonError(description='Invalid value.')
   return json_response(value=value + 1)

   #idjson = data[id]
   #output = {"result": "OK"}
   #output = request.json
   #return jsonify(output)
   #return idjson

@app.route('/json', methods=['GET'])
def retrieve():
   output = {"result": "OK"}
   #output = request.json
   return jsonify(output)

@app.route('/json', methods=['PUT'])
def update():
   output = {"result": "OK"}
   #output = request.json
   return jsonify(output)

def save():
    return "save"
def update():
    return "update"
def check():
    return "check"

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
