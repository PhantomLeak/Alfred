import alfred_games as ag
import alfred as af 
import alfred_feelings as alf
import web_search as ws
import password_generator as pg

#Completes the logic for Alfred
def logic(i) : 
    if ('game' in i) :
        games = input("Which game would you like to play? (1. Rock Paper Scissors, 2. Guessing Game, 3. Quit):  ")
        print("")
        if games == '1' or 'rock' in games or 'paper' in games or 'scissors' in games:
            ag.rock_paper_scissors()
        elif games == '2' or 'guessing' in games:
            ag.guessing_game()
        else:
            print('GoodBye, come play again! \n')
            af.alfred_main(1)

    elif ('search' in i):
        search_input = input("What would you like to search?: ")
        ws.googlesearch(search_input)

    elif ('password' in i):
        pLen = int(input('How long does the password need to be? : '))
        pg.create_password(pLen)

    elif ('exit' or 'end' in i):
        print('I hope you have a great day!')
        exit()
        
    else : 
        print("I'm sorry, I don't quite understand, can you try again? ")
        af.alfred_main(1)
        