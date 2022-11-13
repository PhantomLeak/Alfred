from Games.alfred_games import games
from functions.terminal_colors import colors as terminal_message
import alfred as af
import functions.password_generator as pg
import functions.alfred_jokes as aj
import functions.weather as weather
import functions.calculator as calculator
import functions.clear_temp_data as ctd
import assets.temp_db_object as tbo
# import tests as test
# import web_search as ws

alfredGames = games()
tc = terminal_message()

# Completes the logic for Alfred
def logic(i):
    response = i.strip()
    if response in tbo.game_initiators:
        game_choice = input(tc.prompt_message(f"Which game would you like to play? ({tc.prompt_message_choices('1.','Rock Paper Scissors,')}, {tc.prompt_message_choices('2.','Guessing Game,')}, {tc.prompt_message_choices('3.','Sudoku,')} {tc.prompt_message_choices('4.','Snake Game,')} {tc.prompt_message_choices('5.','Quit):')}"))
        print("")
        if game_choice == '1' or 'rock' in game_choice or 'paper' in game_choice or 'scissors' in game_choice:
            alfredGames.gameDecision('rock_paper_scissors')
        elif game_choice == '2' or 'guessing' in game_choice:
            alfredGames.gameDecision('guessing_game')
        elif game_choice == '3' or 'sudoku' in game_choice:
            alfredGames.gameDecision('sudoku')
        elif game_choice == '4' or 'snake' in game_choice:
            alfredGames.gameDecision('snake_game')
        else:
            print(tc.output_message('GoodBye, come play again!'))
            af.alfred_main(1)

    # elif '?' in i and 'how are you?' not in i:
    #     ws.googlesearch(i)

    elif response in tbo.password_initiators:
        password_length = int(input(tc.prompt_message('How many characters does the password need to be? :')))
        pg.create_password(password_length)

    elif response in tbo.weather_initiators:
        forecast = weather.weather()
        print(tc.output_message(forecast))
        af.alfred_main(1)

    elif response in tbo.local_storage_iniators:
        ctd.clear_local_files()
        af.alfred_main(1)

    elif '+' in response or '-' in response or '/' in response or '*' in response or 'square root' in response or 'squared' in response or 'power of' in response:
        calc = calculator.string_num_seperator(response)
        print(tc.output_message('The Answer is: '+ str(calc) + '\n'))
        af.alfred_main(1)

    elif response in tbo.joke_initiators:
        joke = aj.jokes()
        print(tc.output_message('\n' + '- ' + joke + '\n'))
        anotherJoke = input(tc.prompt_message('Would you like to hear another?:'))
        
        if anotherJoke.lower() == 'y' or anotherJoke.lower() == 'yes':
            logic('joke')
        if anotherJoke.lower() == 'n' or anotherJoke.lower() == 'no':
            af.alfred_main(1)
        else:
            print(tc.error_message("I don't quite understand..."))
            af.alfred_main(1)

    elif i == 'end' or i == 'exit' or i == 'no':
        print(tc.output_message('I hope you have a great day!'))
        exit()

    else:
        user_input = ''
        if i.strip == 'game':
            user_input = input(tc.prompt_message('Do you want to play a game?:')).lower()
            if user_input == 'yes' or user_input == 'y':
                logic("I want to play a game")
        print(tc.error_message("I'm sorry, I don't quite understand, can you try again? "))
        af.alfred_main(1)