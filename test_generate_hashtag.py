import pytest
from generate_hashtag import generate_hashtag

# Handling a single word
def test_generate_hashtag_case_one():
    assert(generate_hashtag('Codewars'))=='#Codewars'

# Handling leading whitespace
def test_generate_hashtag_case_two():
    assert(generate_hashtag('      Codewars'))=='#Codewars'

# Handling trailing whitespace
def test_generate_hashtag_case_three():
    assert(generate_hashtag('Codewars     '))=='#Codewars'

# Removing Spaces
def test_generate_hashtag_case_four():
    assert(generate_hashtag('Codewars Is Nice'))=='#CodewarsIsNice'

# capitalize first letters of words
def test_generate_hashtag_case_five():
    assert(generate_hashtag('codewars is nice'))=='#CodewarsIsNice'

# Only the first letter of each word should be capitalized in the final hashtag, all other letters must be in lower case
def test_generate_hashtag_case_six():
    assert(generate_hashtag('CoDeWaRs is niCe'))=='#CodewarsIsNice'

# A single letter is considered to be a word of length 1, so should capitalize first letters of words of length 1
def test_generate_hashtag_case_seven():
    assert(generate_hashtag('c i n'))=='#CIN'