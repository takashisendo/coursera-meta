import pytest
alpha = "Checking the length & structure of the sentence."
@pytest.fixture
def input_value():
    input_str = alpha
    print(input_str)
    return input_str
sentence = input_value()
def word_count(sentence):
    # Function to check the number of words. Returns the word count in string.
    words = len(sentence.split())
    print(words)
    return words
word_count(alpha)