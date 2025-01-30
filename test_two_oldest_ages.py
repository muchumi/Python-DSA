import pytest
from two_oldest_ages import two_oldest_ages

def test_two_oldest_ages_case_one():
    assert(two_oldest_ages([1, 5, 87, 45, 8, 8])) == [45, 87]

def test_two_oldest_ages_case_two():
    assert(two_oldest_ages([6, 5, 83, 5, 3, 18])) == [18, 83]

def test_two_oldest_ages_case_three():
    assert(two_oldest_ages([10, 1])) == [1, 10]