"""
    Count the number of Duplicates
    Write a function that will return the count of distinct case-insensitive alphabetic characters and 
    numeric digits that occur more than once in the input string. The input string can be assumed to contain 
    only alphabets (both uppercase and lowercase) and numeric digits.
"""

def duplicate_count(text):
    #converting the input text into lowercase to make case insensitive
    text=text.lower()
    #using a set to store characters that have been seen atleast once
    seen=set()
    #using a set to store characters that are duplicates/encountered more than once
    duplicates=set()
    for char in text:
        #If the character is already in the seen set, it is added to the duplicates set.
        if char in seen:
            duplicates.add(char)
        #If the character is not in the seen set, it is added to the seen set.
        else:
            seen.add(char)
    return len(duplicates)

