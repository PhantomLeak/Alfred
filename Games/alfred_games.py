import random  
import alfred as af
#from Games.sudoku_gui import Grid as SudokuGame

mode = ''
#Todo: Create more games...maybe something like the snake game or hangman? come back to this...
##TODO: Randomly generate the sudoku board rather than the prebuilt one...
class games():
    def __init__(self):
        pass

    def gameDecision(self, game):
        if game == 'rock_paper_scissors':
            self.rock_paper_scissors()
        elif game == 'guessing_game':
            self.guessing_game(10)
        elif game == 'sudoku':
            import Games.sudoku_gui as SudokuGame
            self.play_again('sudoku')

            pass
    def play_again(self, mode):
        currentMode = mode
        choice = input("Would you like to try again?: ")
        if choice == "yes" or choice.lower() == 'y':
            if currentMode == 'rock_paper_scissors':
                self.rock_paper_scissors()
            if currentMode == 'sudoku':
                self.gameDecision('sudoku')
        elif choice == "no" or choice.lower() == 'n':
            print('\n Not a problem \n')
            af.alfred_main(1)
        else:
            print("I don't quite understand...please try that again")
            self.play_again(currentMode)

    def rock_paper_scissors(self):
        mode = 'rock_paper_scissors'
        comp = random.randint(1,3)
        typeValue = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        user = int(input(f"choose your weapon (1: {typeValue[1]}, 2: {typeValue[2]}, 3: {typeValue[3]}, 4:Exit): "))
        if user == comp:
            print("Its a tie, try again \n")
            self.rock_paper_scissors()
        elif user == "1" and comp == 2 or user == "2" and comp == 3 or user == "3" and comp == 1:
            print(f"You lose, the computer chose {typeValue[comp]}\n")
            self.play_again(mode)
        elif user == "4":
            af.alfred_main(1)
        else:
            print(f"You win! the computer chose {typeValue[comp]} \n")
            self.play_again(mode)

    #Guessing game (numbers game)
    def guessing_game(self, highNumber):
        number = random.randint(1, highNumber)
        tries = 0
        win = False # setting a win flag to false
        print(f"I'm thinking of a number between 1 & {highNumber}")
        while not win:       # while the win is not true, run the while loop. We set win to false at the start therefore this will always run
            guess = int(input("Have a guess: "))
            tries = tries + 1
            if guess == number:
                 win = True    # set win to true when the user guesses correctly.
            elif guess < number:
                print("Guess Higher")
            elif guess > number:
                 print("Guess Lower")

        print(f"That's Correct!! The number was {number} \n")
        print(f"it took you {tries} tries to get it correct \n")

        next_level = input("Would you like to move to the next level?[Y/N]: ")
        if next_level.lower() == "y":
            self.guessing_game(highNumber + 10)
        elif next_level.lower() == "n":
            print("Well, I hope to see you soon!! \n")
            af.alfred_main(1)