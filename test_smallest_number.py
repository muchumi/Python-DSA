import pytest
from smallest_number import remove_smallest
from numpy.random import randint

def test_for_input_case_one():
    assert(remove_smallest([1, 2, 3, 4, 5]))==[2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]"

def test_for_input_case_two():
    assert(remove_smallest([5, 3, 2, 1, 4]))==[5 ,3 , 2, 4], "Wrong result for [5, 3, 2, 1, 4]"

def test_for_input_case_three():
    assert(remove_smallest([1, 2, 3, 1, 1]))==[2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]"

def test_for_input_case_four():
    assert(remove_smallest([]))==[], "Wrong result for []"

def randlist():
    return list(randint(400, size=randint(1, 10)))

def test_for_mutation_of_original_list():
    # Invoking randlist function to generate the list
    new_list=randlist()
    # Makes a swallow copy
    copy=list(new_list)
    # uses the original list with the function
    remove_smallest(new_list)
    assert(new_list==copy, "You've mutated input list  (expectation assertion is on the value of input list, not method output)")

