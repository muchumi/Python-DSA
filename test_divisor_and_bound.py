import pytest
from divisor_and_bound import max_multiple

def test_divisor_and_bound_case_one():
    assert(max_multiple(2, 7)) == 6

def test_divisor_and_bound_case_two():
    assert(max_multiple(3, 10)) == 9

def test_divisor_and_bound_case_three():
    assert(max_multiple(37, 200)) == 185