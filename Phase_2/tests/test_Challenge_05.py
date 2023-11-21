from lib.Challenge_05 import *


def test_start_text_upper_letter() :
    grammar = GrammarStats()
    assert not grammar.check("this starts with lowercase!")

def test_check_invalid_end():
    grammar = GrammarStats()
    assert not grammar.check("This does not end with exclamation")

def test_check_valid_sentence():
    stats = GrammarStats()
    assert stats.check("This is a valid sentence.")

def test_check_empty_string():
    grammar = GrammarStats()
    assert not grammar.check("")

def test_percentage_good_no_texts():
    grammar = GrammarStats()
    assert grammar.percentage_good() == 0

def test_percentage_good_mixed_sentences():
    stats = GrammarStats()
    stats.check("Valid sentence.")
    stats.check("invalid sentence")
    assert stats.percentage_good() == 50

def test_percentage_good_all_valid():
    stats = GrammarStats()
    stats.check("Good Sentence.")
    stats.check("Another valid one!")
    assert stats.percentage_good() == 100



