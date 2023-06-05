import logging
from src.assets import temp_db_object as tbo
from src.functions import alfred_jokes as aj
from src.functions import calculator as calculator
from src.functions import reminders as reminders
from src.functions import weather as weather
from src.functions import cur_date_time as cur_date_time
from src.functions import web_search as web_search
from src.functions.password_generator import Password as Password
from src.functions.Games.alfred_games import Games

# Class initialization
password = Password()
alfredGames = Games()


# Completes the logic for Alfred
def logic(response: dict = {}):
    operation = response.get('operation')
    payload = response.get('payload')
    try:

        if operation.lower() == 'generate_password':
            new_password = password.create_password(password_obj=payload)

            return new_password

        if operation.lower() == 'get_weather':
            weather_request = payload.get('weather_request')
            return weather.weather(weather_init=weather_request)
        #
        # elif ('+' in response or '-' in response or '/' in response or '*' in response or 'square root' in response
        #       or 'squared' in response or 'power of' in response):
        #     calc = calculator.string_num_seperator(response)
        #     return f'The answer is: {str(calc)}'
        #
        # elif response in tbo.joke_initiators:
        #     joke = aj.jokes()
        #     return joke
        #
        # elif 'open' in response or 'search for' in response:
        #     success = web_search.search_web(response)
        #
        #     return success
        #
        # elif ("todays date" in response or "today's date" in response or "current date" in response
        #       or "current time" in response or "time right now" in response):
        #     date_time = cur_date_time.get_date_time(response=response)
        #
        #     return date_time

        # elif 'set a reminder' in response or 'remind me' in response:
        #     reminders.set_reminder(response)
        #     return 'Reminder Set'

        # elif response == 'help' or response == 'what can you do?' or response == 'what can you do':
        #     return_response = '<span>'
        #     return_response += 'Here are some things I can help you with: <br/>'
        #
        #     for idx, commands in enumerate(tbo.help_options):
        #         return_response += f'<span class="ml-4">{idx + 1}. {commands}</span> <br/>'
        #
        #     return_response += '</span>'
        #
        #     return return_response
        #
        # elif response == 'thank you':
        #     return "It's my pleasure! Let me know if there's anything else I can do for you."

        else:
            return "I'm sorry, I don't quite understand, can you try again?"
    except Exception as e:
        logging.exception(e)
