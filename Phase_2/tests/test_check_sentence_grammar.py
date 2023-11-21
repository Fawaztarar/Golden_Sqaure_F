from lib.check_sentence_grammar import *

def test_with_valid_sentence () :
    result =check_sentence_grammar("Hello, this is a fine day.")
    assert result == True


def test_with_capital_letter_but_no_ending_mark():
    result = check_sentence_grammar ("Hello, this is a fine day")
    assert result == False

def test_with_valid_sentence_upper_questionmark() :
    result = check_sentence_grammar("Hello, this is a fine day?")
    assert result == True

def test_with_valid_sentence_upper_exclaim() :
    result = check_sentence_grammar("Hello, this is a fine day!")
    assert result == True

def test_with_valid_sentence_letter_comma() :
    result = check_sentence_grammar("Hello, this is a fine day,")
    assert result == True

def test_with_valid_sentence_upper_collan() :
    result = check_sentence_grammar("Hello, this is a fine day:")
    assert result == True

def test_with_valid_sentence_lower_fullstop() :
    result = check_sentence_grammar("hello, this is a fine day.")
    assert result == True

