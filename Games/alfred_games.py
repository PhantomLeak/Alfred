import random  
import alfred as af
from Games import snake_game as sg
from terminal_colors import colors as terminal_message
#from Games.sudoku_gui import Grid as SudokuGame

tc = terminal_message()

mode = ''
#Todo: Create more games...maybe something like the snake game or hangman? come back to this...
##TODO: Randomly generate the sudoku board rather than the prebuilt one... Not liking the sudoku game idea anyways...move to remaking snake & maybe pong or space invaders...that could be fun.
class games():
    def __init__(self):
        pass

    def gameDecision(self, game):
        if game == 'rock_paper_scissors':
            self.rock_paper_scissors()
        elif game == 'guessing_game':
            self.guessing_game(10)
        elif game == 'snake_game':
            self.snake_game()

    def play_again(self, mode):
        currentMode = mode
        choice = input(tc.prompt_message("Would you like to try again? (y/n):"))
        if choice == "yes" or choice.lower() == 'y':
            if currentMode == 'rock_paper_scissors':
                self.rock_paper_scissors()
            if currentMode == 'sudoku':
                self.gameDecision('sudoku')
            if currentMode == 'snake_game':
                self.gameDecision('snake_game')
        elif choice == "no" or choice.lower() == 'n':
            print(tc.output_message('Not a problem'))
            af.alfred_main(1)
        else:
            print(tc.error_message("I don't quite understand...please try that again"))
            self.play_again(currentMode)

    def rock_paper_scissors(self):
        mode = 'rock_paper_scissors'
        comp = random.randint(1,3)
        typeValue = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
        print('\n')
        user = int(input(tc.prompt_message(f"choose your weapon ({tc.prompt_message_choices('1.', typeValue[1])}, {tc.prompt_message_choices('2.', typeValue[2],)} {tc.prompt_message_choices('3.', typeValue[3],)} {tc.prompt_message_choices('4.', 'Quit:')})")))
        if user == comp:
            print("Its a tie, try again \n")
            self.rock_paper_scissors()
        elif user == "1" and comp == 2 or user == "2" and comp == 3 or user == "3" and comp == 1:
            print(tc.output_message(f"You lose, the computer chose {typeValue[comp]}\n"))
            self.play_again(mode)
        elif user == "4":
            af.alfred_main(1)
        else:
            print(tc.output_message(f"You win! the computer chose {typeValue[comp]} \n"))
            self.play_again(mode)

    #Guessing game (numbers game)
    def guessing_game(self, highNumber):
        number = random.randint(1, highNumber)
        tries = 0
        win = False # setting a win flag to false
        print('\n')
        print(tc.output_message(f"I'm thinking of a number between {tc.terminal_message(tc.yellow, f'1 & {highNumber}')}"))
        while not win:       # while the win is not true, run the while loop. We set win to false at the start therefore this will always run
            guess = int(input(tc.prompt_message("Have a guess: ")))
            tries = tries + 1
            if guess == number:
                 win = True    # set win to true when the user guesses correctly.
            elif guess < number:
                print(tc.output_message("Guess Higher"))
            elif guess > number:
                 print(tc.output_message("Guess Lower"))

        print(tc.output_message(f"That's Correct!! The number was {number} \n"))
        print(tc.output_message(f"it took you {tries} tries to get it correct \n"))

        next_level = input(tc.prompt_message("Would you like to move to the next level?[Y/N]:")).lower()
        if next_level == 'y' or next_level == 'yes':
            self.guessing_game(highNumber + 10)
        elif next_level == 'n' or next_level == 'no':
            print(tc.output_message("Well, I hope to see you soon!! \n"))
            af.alfred_main(1)

    def snake_game(self):
        sg.run_game()
        self.play_again('snake_game')
