"""
    In this little assignment you are given a string of space separated numbers, 
    and have to return the highest and lowest number.
"""
def high_and_low(numbers):
    # Converting the input string into a list of integers
    numbers = list(map(int, numbers.split()))
    if numbers:
        smallest_number=min(numbers)
        highest_number=max(numbers)
    return f"{highest_number} {smallest_number}"
  

high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
high_and_low("1 2 3")
    

