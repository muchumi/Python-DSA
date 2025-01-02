def is_isogram(string):
    #ensuring that the string is in lowercase
    string = string.lower()
    #Iterate through each character in our string
    for letter in string:
        #check if there is any letter that appears more than once in our string
        if string.count(letter) > 1: 
            return False
    return True

