from lib.extract_uppercase_words import *

def test_extract_uppercase_words_empty():
    assert extract_uppercase_words("") == []


def test_with_lowercase_words():
    assert extract_uppercase_words("hello i am fawaz") == []

def test_with_lowercase_word_uppercase_word():
    assert extract_uppercase_words("hello FAWAZ") == ["FAWAZ"]

def test_mix_with_lowercase_word_uppercase_word():
    assert extract_uppercase_words("hello THIS IS fawaz") == ["THIS" , "IS"]

def test_mix_case_words_dont_count_uppercase_word():
    assert extract_uppercase_words("hello THIS Is fawaz") == ["THIS"]

def test_extract_uppercase_word_without_punctutation():
    assert extract_uppercase_words_with_punctutatuion("hello THIS: Is fawaz") == ["THIS"]