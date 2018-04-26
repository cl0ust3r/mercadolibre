from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/json', methods=['POST'])
def post():
    data = jsonify(request.json)
   return data

if __name__ == '__main__':
    app.run(debug=True)
