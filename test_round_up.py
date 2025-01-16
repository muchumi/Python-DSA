import pytest
from round_up import round_up

def test_for_round_up_case_one():
    assert(round_up(12)) == 15

def test_for_round_up_case_two():
    assert(round_up(22)) == 25