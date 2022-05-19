import random  
import alfred as af

class games():
    def __init__(self):
        pass

    def rock_paper_scissors(self):
        comp = random.randint(1,3)
        user = input("choose your weapon(1 = Rock, 2 = Paper, 3 = Scissors, 4 = Exit): ")
        if user == comp:
            print("Its a tie, try again \n")
            self.rock_paper_scissors()
        elif user == "1" and comp == 2 or user == "2" and comp == 3 or user == "3" and comp == 1:
            print("The computer won \n")
            choice = input("Would you like to try again?: ")
            if choice == "yes":
                self.rock_paper_scissors()
            elif choice == "no":
                af.alfred_main(1)
        elif user == "4":
            af.alfred_main(1)
        else:
            print("You win! \n")
            choice = input("Would you like to try again?: ")
            if choice == "yes":
                self.rock_paper_scissors()
            elif choice == "no":
                af.alfred_main(1)

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