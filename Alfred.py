#So far AI system is working perfectly and doesn't seem to have many bugs (plus they're just features anyways)
import random
import webbrowser
def AI():
    login()
    AISpeak()
    feel = feelings()
    game = games()
    joke = jokes()
    googlesearch() #Finally upgraded to import more then one web browser :)
    rock_paper_scissors()
    calc = calculations()
    guessing_game()
    Tom()

def login():
    username = input("Enter Username: ")
    if username == "Dstoc":
        password = input("Enter password: ")
        if password == "MadMax":
            AISpeak()
        else:
            print("Wrong username or password, please try again")
            login()
    else:
        print("Wrong username or password, Please try again")
        login()


def AISpeak():
    print("")
    speak = random.randint(1,2)
    if speak == 1:
        print("Hello sir, Welcome back")
    elif speak == 2:
        print("Welcome back sir")
    user = input("How can I assist you?: ").lower()
    if user == "What is your name?" or user == "what is your name" or user == "What is your name" or user == "what is your name?":
        print("My name is Watson, I am here to assist your needs")
        AISpeak()
    if user == "how are you?" or user == "how are you doing?" or user ==  "how are you" or user == "how are you doing":
        feelings()
    if user == "i wanna search something" or user == "search":
        googlesearch()
    if user == "i wanna play a game" or user == "lets play a game" or user == "im in the mood to play a game" or user == "game":
        games()
    if user == "calculate" or user == "calc" or user == "calculation" or user == "i wanna calculate something":
        calculations()
    if user == "exit" or user == "end":
        Exit = input("Would you like the exit the program?: ").lower()
        if Exit == "yes":
            print("Please come back again!!")
            exit()
        elif Exit == "no":
            AISpeak()
    if user == "tell me a joke" or user == "i wanna hear a joke":
        jokes()
    if user == "help" or user == "I need help" or user == "Give me options":
        print("some options could be to 'search' or 'tell me a joke' or even ask how I am doing.....That'd be nice.... lol")
    if user == "Tom" or user == "tom":
        Tom()
    else:
        print("I dont understand sir, please try again")
        AISpeak()

            

#Talks to you about your feelings (still in alpha development)
def feelings():
    feel = input("I am doing well sir, and yourself?: ").lower()
    if feel == "i feel well" or feel == "good" or feel == "not to bad" or feel == "i am doing well" or feel == "very well" or feel == "I ai doing well":
        print("Thats wonderful sir")
        day = input("How is your day going so far?: ").lower
        if day == "its going well" or day == "not to bad" or day == "prety good" or day == "good" or day == "awesome":
            print("Well im glad to hear that")
            how = input("Is there anything you would like to do? maybe play a game or tell jokes?: ")
            if how == "lets play a game" or how == "game":
                games()
            elif how == "tell me a joke" or how == "joke":
                jokes()
            elif how == "no":
                print("Well if there is anything you need or want just let me know")
                AISpeak()
            else:
                print("I dont understand, please try again")
                feelings()
        elif day == "bad" or day == "not to well" or day == "its not going well" or day == "horrible":
                  print ("well im sorry sir")
                  Help = input("is there anything I can do to help?: ")
                  if Help == "yes":
                      what = input("What can I do?: ")
                      if what == "lets play a game":
                          rock_paper_scissors()
                      elif what == "just talk to me":
                          feelings()
                      elif what == "no":
                          print("Well let me know if you need anything")
                          AISpeak()
                  if Help == "no":
                    print("Well if there is anything I can do please just ask")
    elif feel == "eh" or feel == "not good" or feel == "bad" or feel == "im not doing so well" or feel == "im not doing good":
        helpingcomp = input("Is there anything I can do to help?: ")
        if helpingcomp == "yes":
            game = input("Would a game help cheer you up?: ")
            if game == "yes":
                games()
            if game == "no":
                print("Well if there is anything, just let me know")
                print("")
                AI()
            helpinghand = input("What is it?: ")
        elif helpingcomp == "no":
            print("Well, Im here if you need anything")
            print("")
            AI()
            
#does a google search for anything you want           
def googlesearch():
    Browser = input("What type of browser would you like to use? Google, Yahoo, or Bing?: ")
    if Browser == "google":
        google = input("What would you like to search?:")
        websearch = "https://www.google.co.in/#q=" + google
        webbrowser.open(websearch)
        print("Loading...")
        again = input("Would you like to enter another search?: ")
        if again == "yes":
            googlesearch()
        elif again == "no":
            AISpeak()
    elif Browser == "yahoo":
        Yahoo = input("What would you like to search?: ")
        websearch = "https://www.yahoo.co.in/#q=" + Yahoo
        webbrowser.open(websearch)
        print("Loading...")
        again = input("Would you like to enter another search?: ")
        if again == "yes":
            googlesearch()
        elif again == "no":
            AISpeak()
    elif Browser == "bing":
        Bing = input("What would you like to bing?: ")
        websearch = "https://www.bing.co.in/#q=" + Bing
        webbrowser.open(websearch)
        print("Loading...")
        again = input("Would you like to enter another search?: ")
        if again == "yes":
            googlesearch()
        elif again == "no":
            AISpeak()
   
#Rock paper scissors game
def rock_paper_scissors():
    comp = random.randint(1,3)
    user = input("choose your wepon(1 = Rock, 2 = Paper, 3 = Scissors, 4 = Exit): ")
    if user == comp:
        print("Its a tie, try again")
        rock_paper_scissors()
    elif user == "1" and comp == 2:
        print("The computer won")
        choice = input("Would you like to try again?: ")
        if choice == "yes":
            rock_paper_scissors()
        elif choice == "no":
            AISpeak()
    elif user == "2" and comp == 3:
        print("The computer won")
        choice = input("Would you like to try again?: ")
        if choice == "yes":
            rock_paper_scissors()
        elif choice == "no":
            AISpeak()
    elif user == "3" and comp == 1:
        print("The computer won")
        choice = input("Would you like to try again?: ")
        if choice == "yes":
            rock_paper_scissors()
        elif choice == "no":
            AISpeak()
    elif user == "4":
        AI()
    else:
        print("You win!")
        choice = input("Would you like to try again?: ")
        if choice == "yes":
            rock_paper_scissors()
        elif choice == "no":
            AISpeak()
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
    print("That's Correct!! The number was {}".format(number))
    print("it took you {} tries to get it correct".format(tries))

    next_level = input("Would you like to move to the next level?[Y/N]: ")
    if next_level.lower() == "y":
        lvl2()
    elif next_level.lower() == "n":
        print("Well, I hope to see you soon!!")
        AISpeak()

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
    print("That's Correct!! The number was {}".format(number))
    print("it took you {} tries to get it correct".format(tries))

    next_level = input("Would you like to move to the next level?[Y/N]: ")
    if next_level.lower() == "y":
        lvl3()
    elif next_level.lower() == "n":
        print("Well, I hope to see you soon!!")
        AISpeak()

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
    print("That's Correct!! The number was {}".format(number))
    print("it took you {} tries to get it correct".format(tries))

    next_level = input("Would you like to move to the next level?[Y/N]: ")
    if next_level.lower() == "y":
        lvl4()
    elif next_level.lower() == "n":
        print("Well, I hope to see you soon!!")
        AISpeak()

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
    print("That's Correct!! The number was {}".format(number))
    print("it took you {} tries to get it correct".format(tries))

    next_level = input("Would you like to move to the next level?[Y/N]: ")
    if next_level.lower() == "y":
        lvl5()
    elif next_level.lower() == "n":
        print("Well, I hope to see you soon!!")
        AISpeak()

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
    print("That's Correct!! The number was {}".format(number))
    print("it took you {} tries to get it correct".format(tries))

    print("Thank you for playing my game, Hope we see you soon!!")
    AISpeak()


#Games the program can run
def games():
    games = input("Which game would you like to play? (rock, paper scissors, and guessing game): ")
    print("")
    if games == "rock paper scissors":
        rock_paper_scissors()
    elif games == "guessing game":
        guessing_game()

def calculations():
    Num1 = 0
    Num2 = 0
    
    Typeofcalc = input("What type of calculation would you like to do?: ")
    if Typeofcalc == "Multiplication" or Typeofcalc == "multiply" or Typeofcalc == "mult":
        Num1 = int(input("Enter the first number: "))
        Num2 = int(input("Enter the second number: "))
        mult = Num1 * Num2
        print(mult)
        Next = input("Would you like to do another calculation?: ")
        if Next == "yes":
            calculations()
        elif Next == "no":
            AISpeak()
    elif Typeofcalc == "div" or Typeofcalc == "division":
        Num1 = int(input("Enter first number: "))
        Num2 = int(input("Enter second number: "))
        div = Num1 / Num2
        print(div)
        Next = input("Would you like to do another calculation?: ")
        if Next == "yes":
            calculations()
        elif Next == "no":
            AISpeak()
    elif Typeofcalc == "add" or Typeofcalc == "addition":
        Num1 = int(input("Enter first number: "))
        Num2 = int(input("Enter second number: "))
        add = Num1 + Num2
        print(add)
        Next = input("Would you like to do another calculation?: ")
        if Next == "yes":
            calculations()
        elif Next == "no":
            AISpeak()
    elif Typeofcalc == "subtract" or Typeofcalc == "sub":
        Num1 = int(input("Enter first number: "))
        Num2 = int(input("Enter second number: "))
        sub = Num1 - Num2
        print(sub)
        Next = input("Would you like to do another calculation?: ")
        if Next == "yes":
            calculations()
        elif Next == "no":
            AISpeak()
    elif Typeofcalc == "exit" or Typeofcalc == "end":
        end = input("Would you like to exit calculations?: ")
        if end == "yes":
            AISpeak()
        if end == "no":
            calculations()
    elif Typeofcalc == "square" or Typeofcalc == "Square":  #NEEDS WORK, THE SQUARE WILL NOT ALLOW A SEQUENCE TO MULT ITSELF (VERY ODD CONSIDERING THE MULTIPLICATION WORKS PERFECTLY)
        Num1 = input("Enter the number you would like to square: ")
        print(Num1 * Num1)
        Next = input("Would you like to do another calculation?: ")
        if Next == "yes":
            calculations()
        elif Next == "no":
            AISpeak()
    elif Typeofcalc == "exponent" or Typeofcalc == "exp": #NEEDS WORK (WTF IS GOING ON THAT IT'S NOT WORKING PROPERLY?)
        num1 = input("Enter number: ")
        num2 = input("Enter exponent: ")
        exp = num1 ** num2
        print(exp)
        Next = input("Would you like to do another calculation?: ")
        if Next == "yes":
            calculations()
        elif Next == "no":
            AISpeak()
    else:
        print("I dont understand, please try again")
        calculations()


def jokes():
    joke = random.randint(1,10)
    if joke == 1:
        print("")
        print("So a lightbulb walks into a hotel, he checks in and the bell hop asks for the lightbulbs luggage"
              " the lightbulb replies.....I don't have any, im traveling light")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 2:
        print("")
        print("What do you call an aligator in a vest?.........an investigator")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 3:
        print("")
        print("Two popsicle's are in a freezer, one popsicle says 'man it's cold in here' and the other popsicle says 'Holly crap a talking popsicle!!'")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 4:
        print("")
        print("Why did the chicken cross the road?....to get to the other side")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 5:
        print("")
        print("So a horse walks into a bar, sits at the table, the bar tender comes up and says 'Why the long face?'")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 6:
        print("")
        print("What do you call a fly with no wings?............A walk!")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 7:
        print("")
        print("So my dog tried to bite some fog yesterday..........he mist")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 7:
        print("")
        print("What do you call a duck with a drug problem?.........a quack addic")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 8:
        print("")
        print("What award did the person who invented the knock knock joke get?.........The no bell prize")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 9:
        print("")
        print("Why did the scarecrow get an award?..........He was out standing in his feild")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()
    elif joke == 10:
        print("")
        print("So I had a dream i was a muffler, I woke up exhausted")
        end = input("Would you like to hear another?: ")
        if end == "yes":
            jokes()
        elif end == "no":
            AISpeak()

def Tom():
    Easteregg = "https://www.youtube.com/watch?v=cqyziA30whE"
    Egg = input("Looks like you've found the easter egg, If you would like to procede type 'yes' otherwise type 'no': ")
    if Egg == "Yes" or Egg == "yes":
        webbrowser.open(Easteregg)
    else:
        AISpeak()

def Help():
    print("Enter what you are waning to eithe talk about or ask, if the program does not know the item you are looking for then please contact support at (239)692-2302")
    
            
AI()
    
