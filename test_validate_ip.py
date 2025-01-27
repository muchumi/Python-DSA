import pytest
from validate_ip import validate_ip

def test_validate_ip_case_one():
    assert(validate_ip('192.168.1.24')) == True

def test_validate_ip_case_two():
    assert(validate_ip('')) == False

def test_validate_ip_case_three():
    assert(validate_ip('abc.def.ghi.jkl')) == False

def test_validate_ip_case_four():
    assert(validate_ip('0.0.0.0')) == True

def test_validate_ip_case_five():
    assert(validate_ip('192.168.1.258')) == False

def test_validate_ip_case_six():
    assert(validate_ip('192.168.1.-1')) == False

def test_validate_ip_case_seven():
    assert(validate_ip('12.24.21')) == False