import pyjokes
# from joke.jokes import *
from random import choice


def jokes():
    joke_choice_one = pyjokes.get_joke(language='en', category='all')
    # joke_choice_two = choice([geek, icanhazdad, chucknorris, icndb])()
    #
    # choices = [joke_choice_one, joke_choice_two]

    # return choice(choices)
    return joke_choice_one
