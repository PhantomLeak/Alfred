import pyjokes

#Todo: Generate a randomizer to get different categories of jokes rather than just programming ones.

def jokes():
    joke = pyjokes.get_joke(language='en', category='all')
    return joke