import pytest
from check_coupon import check_coupon

def test_check_coupon_case_one():
    assert(check_coupon('123','123','September 5, 2014','October 1, 2014')) == True

def test_check_coupon_case_two():
    assert(check_coupon('123a','123','September 5, 2014','October 1, 2014')) == False