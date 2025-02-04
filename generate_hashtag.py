def generate_hashtag(string):
    #Check if all the characters in the string are whitespaces using isspace() method
    if not string or string.isspace():
        return False
    
    # Remove any existing '#' and leading/trailing spaces from string
    string = string.lstrip('#').strip()
    
    if not string:
        return False
    
    # Capitalizing each word and removing spaces
    capitalized_string = ''.join(word.capitalize() for word in string.split())
    
    # Add '#' at the beginning
    hashtag = '#' + capitalized_string
    
    # Check if the hashtag is longer than 140 characters
    if len(hashtag) > 140:
        return False
    
    return hashtag