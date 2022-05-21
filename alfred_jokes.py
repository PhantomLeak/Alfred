import pyjokes

def jokes():
    joke = pyjokes.get_joke(language='en', category='all')
    return joke