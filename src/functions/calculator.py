import logging
import math
import re


# Strip numbers out of string and determine calculation types
def string_num_seperator(string):
    calculations = None
    try:
        nums = re.findall('[0-9]+', string) # Regex function to get all the numbers within the string
        if 'square root' in string or 'sqrt' in string:
            return math.sqrt(int(nums[0]))
        if 'squared' in string:
            return int(nums[0])**2
        if 'power of' in string:
            return int(nums[0])**int(nums[1])
        else:
            calculations = re.findall('[\d\(\)\+\-\*\/\.]', string) # Regex function to find numbers and operators for calculations
    except Exception as e:
        logging.exception(e)

        return eval(''.join(calculations))