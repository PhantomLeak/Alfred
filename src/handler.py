import logging
import os

import alfred as af
import assets.temp_db_object as tbo
import functions.alfred_jokes as aj
import functions.calculator as calculator
import functions.clear_temp_data as ctd
import functions.reminders as reminders
import functions.weather as weather
import functions.web_search as web_search
from functions.Games.alfred_games import Games
from functions.password_generator import Password as Password
from functions.terminal_colors import colors as terminal_message

# Class initialization
alfredGames = Games()
tc = terminal_message()
password = Password()


# Completes the logic for Alfred
def logic(i):
    response = i.strip()
    try:
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

        if response in tbo.password_initiators:
            new_password = password.create_password()

            # print(tc.output_with_return_message('Your new password is:', new_password))
            # af.alfred_main(1)
            return new_password

        # elif 'weather' in response.lower():
        #     forecast = weather.weather(response)
        #     print(tc.output_message(forecast))
        #     af.alfred_main(1)

        # elif response in tbo.local_storage_iniators:
        #     ctd.clear_local_files()
        #     af.alfred_main(1)

        # elif ('+' in response or '-' in response or '/' in response or '*' in response or 'square root' in response
        #       or 'squared' in response or 'power of' in response):
        #     calc = calculator.string_num_seperator(response)
        #     print(tc.output_message('The Answer is: ' + str(calc) + '\n'))
        #     af.alfred_main(1)

        # elif response in tbo.joke_initiators:
        #     joke = aj.jokes()
        #     print(tc.output_message('\n' + '- ' + joke + '\n'))
        #     anotherJoke = input(tc.prompt_message('Would you like to hear another?:'))

        #     if anotherJoke.lower() == 'y' or anotherJoke.lower() == 'yes':
        #         logic('joke')
        #     if anotherJoke.lower() == 'n' or anotherJoke.lower() == 'no':
        #         af.alfred_main(1)
        #     else:
        #         print(tc.error_message("I don't quite understand..."))
        #         af.alfred_main(1)

        # elif 'open' in response or 'search for' in response:
        #     success = web_search.search_web(response)

        #     print(tc.output_message(success))
        #     af.alfred_main(1)

        # elif 'set a reminder' in response or 'remind me' in response:
        #     reminders.set_reminder(response)
        #     af.alfred_main(1)

        # elif response == 'clear':
        #     os.system('cls' if os.name == 'nt' else 'clear')
        #     af.alfred_main(1)

        # elif response == 'help':
        #     print("Here are some of the commands I can help you with: ")

        #     for idx, commands in enumerate(tbo.help_options):
        #         print(tc.output_message(f"{idx}. {commands}"))
        #     af.alfred_main(1)

        # elif i == 'end' or i == 'exit' or i == 'no':
        #     print(tc.output_message('I hope you have a great day!'))
        #     exit()

        # else:
        #     if i.strip == 'game':
        #         user_input = input(tc.prompt_message('Do you want to play a game?:')).lower()
        #         if user_input == 'yes' or user_input == 'y':
        #             logic("I want to play a game")
        #     print(tc.error_message("I'm sorry, I don't quite understand, can you try again? "))
        #     af.alfred_main(1)
    except Exception as e:
        logging.exception(e)
