import math
import re

#TODO: Allow for calculations with multiple operators and more than two numbers,and power operators
# Strip numbers out of string and determine calculation types
def string_num_seperator(string):
    if 'square root' in string or 'sqrt' in string:
        nums = re.findall('[0-9]+', string)
        return math.sqrt(int(nums[0]))
    else:
        calculations = re.findall('[\d\(\)\+\-\*\/\.]', string)

        return eval(''.join(calculations))
