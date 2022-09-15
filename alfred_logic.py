from Games.alfred_games import games
from terminal_colors import colors as terminal_message
import alfred as af
# import tests as test
import web_search as ws
import password_generator as pg
import alfred_jokes as aj
import weather as weather
import calculator as calculator
import clear_temp_data as ctd

alfredGames = games()
tc = terminal_message()

##Todo: Setup a db to hold question requests, answers, and possible initiators to allow alfred to learn.
game_initiators = [
    'i want to play a game',
    'lets play a game',
    "let's play a game",
    'i wanna play a game',
    'i want to play rock paper scissors',
    'lets play rock paper scissors',
    "Let's play rock paper scissors",
    'lets play the guessing game',
    "Let's play the guessing game",
    'lets play guessing game',
    "Let's play guessing game",
]
password_initiators = [
    'i need a password',
    'i need to make a password',
    'make a password',
    'create a password',
    'make me a password'
]
weather_initiators = [
    'tell me the weather',
    'what is the weather gonna be like',
    'how will the weather be today',
    'give me the forcast for today',
    'tell me the weather forcast',
    'weather forecast'
]

joke_initiators = [
    'tell me a joke',
    'can you tell me a joke',
    'can you tell me a joke?',
    'i want to hear something funny'
]

local_storage_iniators = [
    'clear local storage',
    'clear cache',
    'clean computer'
]

# Completes the logic for Alfred
def logic(i):
    response = i.strip()
    if response in game_initiators:
        # game_choice = input(tc.prompt_message("Which game would you like to play? (1. Rock Paper Scissors, 2. Guessing Game, 3.Sudoku 4.Snake Game 5. Quit):"))
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

    elif '?' in i and 'how are you?' not in i:
        ws.googlesearch(i)

    elif response in password_initiators:
        password_length = int(input(tc.prompt_message('How many characters does the password need to be? :')))
        pg.create_password(password_length)

    elif response in weather_initiators:
        forecast = weather.weather()
        print(tc.output_message(forecast))
        af.alfred_main(1)

    elif response in local_storage_iniators:
        ctd.clear_local_files()
        af.alfred_main(1)

    elif '+' in response or '-' in response or '/' in response or '*' in response or 'square root' in response or 'squared' in response or 'power of' in response:
        calc = calculator.string_num_seperator(response)
        print(tc.output_message('The Answer is: '+ str(calc) + '\n'))
        af.alfred_main(1)

    elif response in joke_initiators:
        joke = aj.jokes()
        print(tc.output_message('\n' + '- ' + joke + '\n'))
        anotherJoke = input(tc.prompt_message('Would you like to hear another?:'))
        if anotherJoke.lower() =='y' or anotherJoke.lower() =='yes':
            logic('joke')
        if anotherJoke.lower() =='n' or anotherJoke.lower() =='no':
            af.alfred_main(1)
        else:
            print(tc.error_message("I don't quite understand..."))
            af.alfred_main(1) #TODO fild better solution for this...

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

