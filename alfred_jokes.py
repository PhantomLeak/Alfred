import pyjokes
from joke.jokes import *
from random import choice
#Todo: Generate a randomizer to get different categories of jokes rather than just programming ones.

def jokes():
    joke_choice_one = pyjokes.get_joke(language='en', category='all')
    joke_choice_two = choice([geek, icanhazdad, chucknorris, icndb])()

    choices = [joke_choice_one, joke_choice_two]
    
    return choice(choices)