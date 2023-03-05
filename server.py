from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from src.handler import logic
from src.functions.greeting import greeting
import logging

# Config
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={f'/*': {'origins': '*'}})


@app.route('/', methods=['GET', 'POST'])
def alfred():
    response_obj = {}

    if request.method == 'POST':
        try:
            post_data = request.get_json()
            request_msg = post_data.get('request_msg')
            return_response = logic(request=request_msg)
            response_obj = {'response': 200, 'return_msg': return_response}
        except Exception as e:
            logging.exception(e)
            response_obj = {'response': 404}

    if request.method == 'GET':
        try:
            greeting_msg = greeting()
            response_obj = {'response': 200, 'greeting_msg': greeting_msg}
        except Exception as e:
            logging.exception(e)
            response_obj = {'response': 404}

    return jsonify(response_obj)


if __name__ == '__main__':
    app.run()
