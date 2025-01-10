import pytest
from get_middle import get_middle

def test_for_middle_case_one():
    assert(get_middle("test"),"es")

def test_for_middle_case_two():
    assert(get_middle("testing"), "t")

def test_for_middle_case_three():
    assert(get_middle("middle"), "dd")

def test_for_middle_case_four():
    assert(get_middle("A"), "A")

def test_for_middle_case_five():
    assert(get_middle("of"), "of")