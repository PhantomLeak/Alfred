from Games.alfred_games import games
import alfred as af
import tests as test
import web_search as ws
import password_generator as pg
import alfred_jokes as aj
import weather as weather

alfredGames = games()


# Completes the logic for Alfred
def logic(i):
    if ('game' in i):
        games = input("Which game would you like to play? (1. Rock Paper Scissors, 2. Guessing Game, 3.Sudoku 4. Quit):  ")
        print("")
        if games == '1' or 'rock' in games or 'paper' in games or 'scissors' in games:
            alfredGames.gameDecision('rock_paper_scissors')
        elif games == '2' or 'guessing' in games:
            alfredGames.gameDecision('guess_game')
        elif games == '3' or 'sudoku' in games:
            alfredGames.gameDecision('sudoku')
        else:
            print('GoodBye, come play again! \n')
            af.alfred_main(1)

    elif ('?' in i):
        ws.googlesearch(i)

    elif ('password' in i):
        pLen = int(input('How long does the password need to be? : '))
        pg.create_password(pLen)

    elif ('weather' in i):
        forecast = weather.weather()
        print(forecast + '\n')
        af.alfred_main(1)

    elif (i == 'test'):
        result = test.scrape_google('dogs')
        print(result)

    elif ('joke' in i):
        joke = aj.jokes()
        print( '\n' + '- ' + joke + '\n')
        anotherJoke = input('Would you like to hear another?: ')
        if anotherJoke.lower() =='y' or anotherJoke.lower() =='yes':
            logic('joke')
        if anotherJoke.lower() =='n' or anotherJoke.lower() =='no':
            af.alfred_main(1)
        else:
            print("I don't quite understand...")
            af.alfred_main(1) #TODO fild better solution for this...

    elif ('exit' or 'end' in i):
        print('I hope you have a great day!')
        exit()

    else:
        print("I'm sorry, I don't quite understand, can you try again? ")
        af.alfred_main(1)
