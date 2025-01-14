import pytest
from binary_to_integer import binary_to_integer

def test_binary_to_integer_case_one():
    assert(binary_to_integer([0,0,0,1]), 1)

def test_binary_to_integer_case_two():
    assert(binary_to_integer([0,0,1,0]), 2)

def test_binary_to_integer_case_three():
    assert(binary_to_integer([1,1,1,1]), 15)

def test_binary_to_integer_case_four():
    assert(binary_to_integer([0,1,1,0]), 6)