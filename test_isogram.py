import pytest
from isogram import is_isogram

def test_is_isogram_with_unique_characters():
    assert is_isogram("abcdef") == True

def test_is_isogram_with_repeated_characters():
    assert is_isogram("monogram") == False

def test_is_isogram_an_empty_string():
    assert is_isogram("") == True
  
