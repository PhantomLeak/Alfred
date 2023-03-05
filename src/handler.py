import logging
from src.assets import temp_db_object as tbo
from src.functions import alfred_jokes as aj
from src.functions import calculator as calculator
from src.functions import reminders as reminders
from src.functions import weather as weather
from src.functions import web_search as web_search
from src.functions.password_generator import Password as Password
from src.functions.Games.alfred_games import Games

# Class initialization
password = Password()
alfredGames = Games()


# Completes the logic for Alfred
def logic(request: str = ''):
    response = request.lower().strip()
    try:
        ## -- NEED TO REWRITE THE GAME HANDLER AND FUNCTIONS -- ##

        # if 'game' in response:
        #     if 'snake' in response:
        #         alfredGames.gameDecision('snake_game')

        #     return 'loading...'
        # if response in tbo.game_initiators:
        #     game_choice = input(tc.prompt_message(
        #         f"Which game would you like to play? ({tc.prompt_message_choices(1, 'Rock Paper Scissors,')}, {tc.prompt_message_choices(2, 'Guessing Game,')}, {tc.prompt_message_choices(3, 'Sudoku,')} {tc.prompt_message_choices(4, 'Snake Game,')} {tc.prompt_message_choices(5, 'Quit):')}"))
        #     print("")
        #     if game_choice == '1' or 'rock' in game_choice or 'paper' in game_choice or 'scissors' in game_choice:
        #         alfredGames.gameDecision('rock_paper_scissors')
        #     elif game_choice == '2' or 'guessing' in game_choice:
        #         alfredGames.gameDecision('guessing_game')
        #     elif game_choice == '3' or 'sudoku' in game_choice:
        #         alfredGames.gameDecision('sudoku')
        #     elif game_choice == '4' or 'snake' in game_choice:
        #         alfredGames.gameDecision('snake_game')
        #     else:
        #         print(tc.output_message('GoodBye, come play again!'))
        #         af.alfred_main(1)

        if 'password' in response:
            new_password = password.create_password(password_init=response)

            return new_password

        elif 'weather' in response.lower():
            forecast = weather.weather(response)
            return forecast

        elif ('+' in response or '-' in response or '/' in response or '*' in response or 'square root' in response
              or 'squared' in response or 'power of' in response):
            calc = calculator.string_num_seperator(response)
            return f'The answer is: {str(calc)}'

        elif response in tbo.joke_initiators:
            joke = aj.jokes()
            return joke

        elif 'open' in response or 'search for' in response:
            success = web_search.search_web(response)

            return success

        elif 'set a reminder' in response or 'remind me' in response:
            reminders.set_reminder(response)
            return 'Reminder Set'

        elif response == 'help':
            return_response = ''
            return_response += 'Here are some of the commands I can help you with: '

            for idx, commands in enumerate(tbo.help_options):
                return_response += f'{idx}. {commands}'

            return return_response

        else:
            return "I'm sorry, I don't quite understand, can you try again?"
    except Exception as e:
        logging.exception(e)
