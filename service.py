import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request
from flask_restful import Resource, Api, abort

app = Flask(__name__)
api = Api(app)

ids = {}

def abort_request(id):
    if id not in ids:
        abort(404, message="ID {} doesn't exist".format(id))


class service(Resource):

    def post(self, id):

        ids[id] = request.form['data']
        app.logger.info('INFO:')
        return {id: ids[id]}

    def get(self, id):
        app.logger.info('INFO:')
        return {id: ids[id]}

    def delete(self, id):
        abort_request(id)
        app.logger.info('INFO:')
        del ids[id]
        return '', 204

    def put(self, id):
        ids[id] = request.form['data']
        app.logger.info('INFO:')
        return {id: ids[id]}

api.add_resource(service, '/json/<string:id>')

if __name__ == '__main__':
    handler = RotatingFileHandler('service.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run("0.0.0.0", port=5000)
