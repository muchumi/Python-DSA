import pytest
from checkout_time import checkout_time

def test_for_wrong_answer_if_the_queue_is_empty():
    assert(checkout_time([], 1), 0, "wrong answer for case with an empty queue")

def test_for_wrong_answer_if_there_is_a_single_person_in_queue():
    assert(checkout_time([5], 1), 5, "wrong answer for a single person in the queue")

def test_for_wrong_answer_for_a_single_till():
    assert(checkout_time([1,2,3,4,5], 1), 15, "wrong answer for a single till")

def test_for_wrong_answer_for_a_large_number_of_tills():
    assert(checkout_time([1,2,3,4,5], 100), 5, "wrong answer for a case with a large number of tills")

def test_for_wrong_answer_for_two_tills():
    assert(checkout_time([2,2,3,3,4,4], 2), 9, "wrong answer for a case with two tills")