# Import statements
import pytest
import spellcheck

# String variable to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"

# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    input_str = alpha
    return input_str


# First test function test_length()
def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars. """

    # Get the input string
    string = input_value

    # Check the number of words
    assert spellcheck.word_count(string) < 10, "String has more than 10 words"

    # Check the number of characters
    assert spellcheck.char_count(string) < 50, "String has more than 50 characters"


# Second test function test_struc()
def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period. """

    # Get the input string
    string = input_value

    # Check if the first character is in upper case
    assert spellcheck.first_char(string).isupper(), "First character is not in upper case"

    # Check if the string ends with a dot
    assert spellcheck.last_char(string) == ".", "String does not end with a dot"


# Run these tests with `python3 -m pytest test_spellcheck.py`
def main():
    test_length(input_value())
    test_struc(input_value())


if __name__ == "__main__":
    main()
