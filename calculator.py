import math
import re

#TODO: Allow for calculations with multiple operators and more than two numbers,and power operators
# Strip numbers out of string and determine calculation types
def string_num_seperator(string):
    nums = re.findall('[0-9]+', string)
    if 'square root' in string or 'sqrt' in string:
        return math.sqrt(int(nums[0]))
    if 'squared' in string:
        return int(nums[0])**2
    if 'power of' in string:
        return int(nums[0])**int(nums[1])
    else:
        calculations = re.findall('[\d\(\)\+\-\*\/\.]', string)

        return eval(''.join(calculations))