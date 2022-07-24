import math
import re

#TODO: Allow for calculations with multiple operators and more than two numbers, and power operators
# Strip numbers out of string and determine calculation types
def string_num_seperator(string):
    operator = None
    # Regex check to find all numbers inside the string
    nums = re.findall('[0-9]+', string)
    if 'plus' in string or '+' in string:
        operator = '+'
    elif 'minus' in string or '-' in string:
        operator = '-'
    elif 'times' in string or '*' in string:
        operator = '*'
    elif 'division' in string or '/' in string:
        operator = '/'
    elif 'sqrt' in string or 'square root' in string:
        operator = 'sqrt'

    return calculations(operator, nums)

#perform calculations and return answer
def calculations(operator, nums):
    if operator == 'sqrt':
        return math.sqrt(int(nums[0]))
    else:
        return eval('{}{}{}'.format(nums[0], operator, nums[1]))
