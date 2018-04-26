import json
import os
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
FlaskJSON(app)

'''



@app.route('/get_value')
@as_json
def get_value():
    return dict(value=12)
'''
@app.route('/json/<string:id>', methods=['GET'])
def get(id):
    return read(id)



@app.route('/json', methods=['POST'])
def post():
    data = request.get_json(force=True)
    try:
        id = str(data['id'])
        value = json_response(id=id)
        save(id, data)

    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Valor Invalido')
    return value


def save(id, data):
    try:
        with open('registro/'+id, 'w') as outfile:
            json.dump(data, outfile)
    except (KeyError, TypeError, ValueError):
        return "Error Desconocido"


def read(id):
    file = os.path.join('registro/', id)
    with open(file) as loadid:
        getdata =json.load(loadid)
    return getdata
def delete(id):
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
