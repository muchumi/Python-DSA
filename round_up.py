import math

"""
    Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
"""

def round_up(number):
    # math.ceil() function rounds up the result to the nearest integer.
    # The rounded integer is then multiplied by 5 to get the next multiple of 5.
    rounded_number=math.ceil(number/5)*5
    return rounded_number

round_up(12)
round_up(22)