"""
    You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.
    If the string's length is odd, return the middle character.
    If the string's length is even, return the middle 2 characters.
"""

def get_middle(string):
    middle=int(len(string)/2)
    if len(string)%2==0:
        return string[middle-1:middle+1]
    else:
        return string[middle]
    
get_middle("test")
get_middle("testing")
get_middle("middle")
get_middle("A")
get_middle("of")