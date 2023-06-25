def decipher_operation(msg):
    if 'weather' in msg:
        return 'get_weather'
    elif 'joke' in msg:
        return 'generate_joke'
    elif contains_equation(msg):
        return 'solve_equation'
    elif "todays date" in msg or "today's date" in msg or "current date" in msg:
        return 'return_date_time'
    elif len(msg.split()) == 2 and msg.partition(' ')[0] == 'open':
        return 'open_url'
    elif msg == 'help':
        return 'return_help_hints'
    elif msg == 'thank you':
        return 'thank_you_return'


def contains_equation(exp):
    operators = ['+', '-', '/', '%', '^', '*', 'square root', 'squared', 'power of']
    if any(char.isdigit() for char in exp) and any(operator in operators for operator in exp):
        return True
    else:
        return False


if __name__ == '__main__':
    test = decipher_operation('What is 7 * 5')
    print(test)
