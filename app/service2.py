from datetime import datetime
from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)
FlaskJSON(app)

'''
@app.route('/get_time')
def get_time():
    now = datetime.utcnow()
    return json_response(time=now)
'''

@app.route('/json', methods=['POST'])
def post():
    data = request.get_json(force=True)
    try:
        id = int(data['id'])
        save(id, data)
    except (KeyError, TypeError, ValueError):
        raise JsonError(description='Invalid value.')
    return json_response(id=id)

'''
@app.route('/get_value')
@as_json
def get_value():
    return dict(value=12)
'''
def save(id, data):
    with open("id.json","wb") as fo:
        fo.write(data)
if __name__ == '__main__':
    app.run()
