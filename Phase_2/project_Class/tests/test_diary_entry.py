from lib.diary_entry import *

def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry ("My Title", "My Contents")
    assert diary_entry.title == "My Title" 

    assert diary_entry.contents == "My Contents"


def test_count_words_returns_word_count_of_contents():
        diary_entry = DiaryEntry ("My Title", "one two thee four five")
        assert diary_entry.count_words() == 5