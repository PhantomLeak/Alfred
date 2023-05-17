from flask import Flask, request, render_template, jsonify, send_file
from flask_cors import CORS
from src.handler import logic
from src.functions.greeting import greeting
from src.functions.imitari import reformat_image
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
    return_response = []

    if request.method == 'POST':
        try:
            post_data = request.get_json()
            request_msg = post_data.get('request_msg')
            return_response = logic(response=request_msg)
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

@app.route('/imitari', methods=['POST'])
def imitari():
    response_obj = {}
    try:
        post_data = request.get_json()
        image = post_data.get('image')
        height = post_data.get('height', 500)
        width = post_data.get('width', 500)
        format_type = post_data.get('fileType', 'PNG')

        if not image:
            return jsonify({'response': 404})

        new_image = reformat_image(image=image, width=int(width), height=int(height), format_type=format_type)

        response_obj = {'response': 200, 'image': new_image}
        return jsonify(response_obj)

    except Exception as e:
        logging.exception(e)
        response_obj = {'response': 404}
        return jsonify(response_obj)


if __name__ == '__main__':
    app.run()

### LIST OF TASKS TO BE COMPLETED
# TODO: Allow Alfred to do speech to text recognition so I can speak to him rather than typing (Kinda like Iron man and Jarvis)
# TODO: Connect to DB and saved responses / questions for ML
# TODO: Allow Alfred to set reminders / write to Google Calendar...
