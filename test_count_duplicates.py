import pytest
from count_duplicates import duplicate_count

def test_count_duplicates_case_one():
    assert(duplicate_count(""))==0

def test_count_duplicates_case_two():
    assert(duplicate_count("abcde"))==0

def test_count_duplicates_case_three():
    assert(duplicate_count("abcdeaa"))==1

def test_count_duplicates_case_four():
    assert(duplicate_count("abcdeaB"))==2

def test_count_duplicates_case_five():
    assert(duplicate_count("Indivisibilities"))==2