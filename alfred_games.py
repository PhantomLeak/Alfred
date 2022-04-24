import random  
import alfred as af
def rock_paper_scissors():
    
    comp = random.randint(1,3)
    user = input("choose your wepon(1 = Rock, 2 = Paper, 3 = Scissors, 4 = Exit): ")
    if user == comp:
        print("Its a tie, try again \n")
        rock_paper_scissors()
    elif user == "1" and comp == 2:
        print("The computer won \n")
        choice = input("Would you like to try again?: ")
        if choice == "yes":
            rock_paper_scissors()
        elif choice == "no":
            af.alfred_main(1)
    elif user == "2" and comp == 3:
        print("The computer won \n")
        choice = input("Would you like to try again?: ")
        if choice == "yes":
            rock_paper_scissors()
        elif choice == "no":
            af.alfred_main(1)
    elif user == "3" and comp == 1:
        print("The computer won \n")
        choice = input("Would you like to try again?: ")
        if choice == "yes":
            rock_paper_scissors()
        elif choice == "no":
            af.alfred_main(1)
    elif user == "4":
        af.alfred_main(1)
    else:
        print("You win! \n")
        choice = input("Would you like to try again?: ")
        if choice == "yes":
            rock_paper_scissors()
        elif choice == "no":
            af.alfred_main(1)
#Guessing game (numbers game)
def guessing_game():
    
    number = random.randint(1, 10)
    tries = 0
    win = False # setting a win flag to false

    name = input("Hello player, What is your name: ")

    print("Hello " + name + "." )

    print("")
    question = input("Would you like to play a game? [Y/N] ")
    if question.lower() == "n": #in case of capital letters is entered
        print("oh..okay")
        exit()
    if question.lower() == "y":
        print("I'm thinking of a number between 1 & 10")
    while not win:       # while the win is not true, run the while loop. We set win to false at the start therefore this will always run
        guess = int(input("Have a guess: "))
        tries = tries + 1
        if guess == number:
             win = True    # set win to true when the user guesses correctly.
        elif guess < number:
            print("Guess Higher")
        elif guess > number:
             print("Guess Lower")
    else:
        question
    # if win is true then output message
    print(f"That's Correct!! The number was {number} \n")
    print(f"it took you {tries} tries to get it correct \n")

    next_level = input("Would you like to move to the next level?[Y/N]: ")
    if next_level.lower() == "y":
        lvl2()
    elif next_level.lower() == "n":
        print("Well, I hope to see you soon!! \n")
        af.alfred_main(1)

def lvl2(): #This is an attempt to make more then one level (I don't know if it will work or not)

    number = random.randint(1, 20)
    tries = 0
    win = False # setting a win flag to false
    
    print("")
    question = input("Would you like to play round two? [Y/N] ")
    if question.lower() == "n": #in case of capital letters is entered
        print("oh..okay")
        exit()
    if question.lower() == "y":
        print("I'm thinking of a number between 1 & 20")
    while not win:       # while the win is not true, run the while loop. We set win to false at the start therefore this will always run
        guess = int(input("Have a guess: "))
        tries = tries + 1
        if guess == number:
             win = True    # set win to true when the user guesses correctly.
        elif guess < number:
            print("Guess Higher")
        elif guess > number:
             print("Guess Lower")
    else:
        question
    # if win is true then output message
    print(f"That's Correct!! The number was {number} \n")
    print(f"it took you {tries} tries to get it correct \n")

    next_level = input("Would you like to move to the next level?[Y/N]: ")
    if next_level.lower() == "y":
        lvl2()
    elif next_level.lower() == "n":
        print("Well, I hope to see you soon!! \n")
        af.alfred_main(1)

def lvl3(): #Turns out I figured out how to work more then one level (must take advantage of this)

    number = random.randint(1, 30)
    tries = 0
    win = False # setting a win flag to false
    
    print("")
    question = input("Would you like to play round three? [Y/N] ")
    if question.lower() == "n": #in case of capital letters is entered
        print("oh..okay")
        exit()
    if question.lower() == "y":
        print("I'm thinking of a number between 1 & 30")
    while not win:       # while the win is not true, run the while loop. We set win to false at the start therefore this will always run
        guess = int(input("Have a guess: "))
        tries = tries + 1
        if guess == number:
             win = True    # set win to true when the user guesses correctly.
        elif guess < number:
            print("Guess Higher")
        elif guess > number:
             print("Guess Lower")
    else:
        question
    # if win is true then output message
    print(f"That's Correct!! The number was {number} \n")
    print(f"it took you {tries} tries to get it correct \n")

    next_level = input("Would you like to move to the next level?[Y/N]: ")
    if next_level.lower() == "y":
        lvl2()
    elif next_level.lower() == "n":
        print("Well, I hope to see you soon!! \n")
        af.alfred_main(1)

def lvl4(): 

    number = random.randint(1, 40)
    tries = 0
    win = False # setting a win flag to false

    print("")
    question = input("Would you like to play round four? [Y/N] ")
    if question.lower() == "n": #in case of capital letters is entered
        print("oh..okay")
        exit()
    if question.lower() == "y":
        print("I'm thinking of a number between 1 & 40")
    while not win:       # while the win is not true, run the while loop. We set win to false at the start therefore this will always run
        guess = int(input("Have a guess: "))
        tries = tries + 1
        if guess == number:
             win = True    # set win to true when the user guesses correctly.
        elif guess < number:
            print("Guess Higher")
        elif guess > number:
             print("Guess Lower")
    else:
        question
    # if win is true then output message
    print(f"That's Correct!! The number was {number} \n")
    print(f"it took you {tries} tries to get it correct \n")

    next_level = input("Would you like to move to the next level?[Y/N]: ")
    if next_level.lower() == "y":
        lvl2()
    elif next_level.lower() == "n":
        print("Well, I hope to see you soon!! \n")
        af.alfred_main(1)

def lvl5():

    number = random.randint(1, 50)
    tries = 0
    win = False # setting a win flag to false
    
    print("")
    question = input("Would you like to play round five? [Y/N] ")
    if question.lower() == "n": #in case of capital letters is entered
        print("oh..okay")
        exit()
    if question.lower() == "y":
        print("I'm thinking of a number between 1 & 50")
    while not win:       # while the win is not true, run the while loop. We set win to false at the start therefore this will always run
        guess = int(input("Have a guess: "))
        tries = tries + 1
        if guess == number:
             win = True    # set win to true when the user guesses correctly.
        elif guess < number:
            print("Guess Higher")
        elif guess > number:
             print("Guess Lower")
    else:
        question
    # if win is true then output message
    print(f"That's Correct!! The number was {number} \n")
    print(f"it took you {tries} tries to get it correct \n")

    print("Thank you for playing my game, Hope we see you soon!!")
    af.alfred_main(1)
