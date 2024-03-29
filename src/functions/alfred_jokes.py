import json
import logging
from random import choice

import pyjokes
import requests


def jokes():
    choices = ''
    try:
        joke_choice_one = pyjokes.get_joke(language='en', category='all')

        joke_choice_two = joke_two_api_call()

        choices = [joke_choice_one, joke_choice_two]

    except Exception as e:
        logging.exception(e)

    return choice(choices)


def joke_two_api_call():
    # https://holypython.com/official-jokes-api/
    data = requests.get('https://official-joke-api.appspot.com/random_joke')
    data_return = json.loads(data.text)

    return f"{data_return['setup']}...{data_return['punchline']}"
