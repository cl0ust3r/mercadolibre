import json
import os
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response

app = Flask(__name__)
FlaskJSON(app)


@app.route('/json/<string:id>', methods=['GET'])
def get(id):
    try:
        value = read(id)
        return str(value)
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='No existe registro')

@app.route('/json/<string:id>', methods=['DELETE'])
def delete(id):
    try:
        remove(id)
        return "DELETE"
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='No existe registro')


@app.route('/json', methods=['PUT'])
def put():
    data = request.get_json(force=True)
    try:
        id = str(data['id'])
        remove(id)
        save(id, data)

        return "UPDATED"
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='No existe registro')


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
    try:
        file = os.path.join('registro/', id)
        with open(file) as loadid:
            getdata =json.load(loadid)
        return getdata

    except (KeyError, TypeError, ValueError):
        return "Error Desconocido"

def remove(id):
    os.remove('registro/'+id)


if __name__ == '__main__':
    app.run(debug=True)
