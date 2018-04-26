import json
import os
from flask import Flask, request
from flask import jsonify
from flask_json import FlaskJSON, JsonError, json_response

app = Flask(__name__)
FlaskJSON(app)


@app.route('/json/<int:id>', methods=['GET'])
def get(id):
    try:
        value = read(str(id))
        return jsonify(value)
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='No existe registro')

@app.route('/json/<int:id>', methods=['DELETE'])
def delete(id):
    try:
        remove(str(id))
        return "Registro Borrado"
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='No existe registro')


@app.route('/json', methods=['PUT'])
def put():
    data = request.get_json(force=True)
    try:
        id = int(data['id'])
        save(str(id), data)

        return "Registro Actualizado"
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='No existe registro')


@app.route('/json', methods=['POST'])
def post():
    data = request.get_json(force=True)
    try:
        id = int(data['id'])
        value = json_response(id=id)
        save(str(id), data)

    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Valor Invalido')
    return value


def save(id, data):
    try:
        with open('registro/'+id, 'w') as outfile:
            json.dump(data, outfile)
    except (KeyError, TypeError, ValueError):
        return "Error Guardando Registro"


def read(id):
    try:
        file = os.path.join('registro/', id)
        with open(file) as loadid:
            getdata =json.load(loadid)
        return getdata

    except (KeyError, TypeError, ValueError):
        return "Error leyendo el Registro"

def remove(id):
    try:
        os.remove('registro/'+id)
    except (KeyError, TypeError, ValueError):
        return "Error Borrando Registro"


if __name__ == '__main__':
    app.run(debug=True)
