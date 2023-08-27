from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
import json

app = Flask(__name__)

CORS(app)

@app.route('/hynoti/hyin', methods=['POST'])
def hy_in():
    return jsonify(json.loads(response))

@app.route('/hynoti/hyie', methods=['POST'])
def hy_ie():
    return jsonify(json.loads(response))

@app.route('/hynoti/chat', methods=['POST'])
def make_chat():
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
