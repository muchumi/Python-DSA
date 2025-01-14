"""
    Given an array of ones and zeroes, convert the equivalent binary value to an integer.
    Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
    However, the arrays can have varying lengths, not just limited to 4.
"""

def binary_to_integer(array):
    # Converting the list of 0s and 1s to a string
    string=''.join(map(str, array))
    # Converting the binary string to an integer
    return int(string, 2)

binary_to_integer([0, 0, 0, 1])

