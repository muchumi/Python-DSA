"""
    Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. 
    IPs should be considered valid if they consist of four octets, with values between 
    0 and 255, inclusive.
"""
def validate_ip(string)->bool:
    #splitting the input string by dot (.)
    new_string=string.split('.')
    #checking if there are exactly four octets
    if len(new_string) != 4:
        return False
    for num in new_string:
        #checking if the num is a valid number and has no extra characters
        if not num.isdigit():
            return False
        #converting into an integer 
        character = int(num)
        #checking if the number is in the valid range[0, 255]
        if character < 0 or character > 255:
            return False
        #checking for a leading zero for any number other than "0"
        if num != str(character):
            return False
    return True