import pytest
from high_and_low import high_and_low

def test_high_and_low_case_one():
    assert(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")

def test_high_and_low_case_two():
    assert(high_and_low("1 2 3"), "3 1")