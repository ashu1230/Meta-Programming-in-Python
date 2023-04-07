# Import pytest and spellcheck modules
import pytest
import spellcheck

# String variables to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    input = alpha
    return input

# First test function test_length()
def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars.
    """
    # Check if the given string has fewer than 10 words
    assert spellcheck.word_count(input_value) < 10

    # Check if the given string has fewer than 50 chars
    assert spellcheck.char_count(input_value) < 50

# Second test function test_struc()
def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period.
    """
    # Check if the given string begins with a capital letter
    assert spellcheck.first_char(input_value).isupper()

    # Check if the given string ends with a period ('.')
    assert spellcheck.last_char(input_value) == '.'

# Run these tests with `python3 -m pytest test_spellcheck.py`
