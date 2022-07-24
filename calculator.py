import math

nums = []
# Strip numbers out of string and determine calculation types
def string_num_seperator(string):
    global calc
    for s in string:
        if s.isdigit():
            nums.append(s)
    if 'plus' in string or '+' in string:
        calc = calculations('+')
    elif 'minus' in string or '-' in string:
        calc = calculations('-')
    elif 'times' in string or '*' in string:
        calc = calculations('*')
    elif 'division' in string or '/' in string:
        calc = calculations('/')
    elif 'square root' in string or 'sqrt' in string:
        calc = calculations('sqrt')

    return calc

#perform calculations and return answer
def calculations(operator):
    if operator == 'sqrt':
        return math.sqrt(nums[0])
    else:
        return eval('{}{}{}'.format(nums[0], operator, nums[1]))

