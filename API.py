
import flask
from flask import request, jsonify
from flask_cors import CORS
from pychatgpt import Chat, Options

app = flask.Flask(__name__)
CORS(app)



@app.route('/')
def chat():

    gpt = Chat(email="", password="")
    answer = gpt.ask("How are you?")
    

    return jsonify(answer)

app.run(debug=True, host='0.0.0.0')