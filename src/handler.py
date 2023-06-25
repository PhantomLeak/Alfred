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
from src.common_functions import decipher_operation
# Class initialization
password = Password()
alfredGames = Games()


# Completes the logic for Alfred
def logic(response: dict = {}):
    operation = response.get('operation')
    payload = response.get('payload')
    msg = payload.get('msg')
    if not operation:
        operation = decipher_operation(msg)
    try:
        if operation.lower() == 'generate_password':
            new_password = password.create_password(password_obj=payload)

            return new_password

        elif operation.lower() == 'get_weather':
            return weather.weather(weather_init=msg)

        elif operation.lower() == 'generate_joke':
            return aj.jokes()

        elif operation.lower() == 'solve_equation':
            calc = calculator.string_num_seperator(string=msg)
            return f'The answer is: {str(calc)}'

        elif operation.lower() == 'return_date_time':
            return cur_date_time.get_date_time(response=msg)

        elif operation.lower() == 'open_url':
            return web_search.search_web(search_request=msg)

        elif operation.lower() == 'return_help_hints':
            return_response = '<span>'
            return_response += 'Here are some things I can help you with: <br/>'

            for idx, commands in enumerate(tbo.help_options):
                return_response += f'<span class="ml-4">{idx + 1}. {commands}</span> <br/>'

            return_response += '</span>'

            return return_response

        elif operation.lower() == 'thank_you_return':
            return "It's my pleasure! Let me know if there's anything else I can do for you."

        # elif 'set a reminder' in response or 'remind me' in response:
        #     reminders.set_reminder(response)
        #     return 'Reminder Set'


        else:
            return "I'm sorry, I don't quite understand, can you try again?"
    except Exception as e:
        logging.exception(e)
