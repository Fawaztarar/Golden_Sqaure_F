import pytest
from lib.diary_entry import *


def test_formats_with_title_and_contents() :
    diary_entry = DiaryEntry ("My Title", "Some contents")
    result = diary_entry. format ()
    assert result == "My Title: Some contents"

def test_count_words_title_and_contents() :
    diary_entry = DiaryEntry ("My Title", "Some contents")
    result = diary_entry. count_words ()
    assert result == 4

def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    assert str(err.value) == "Diary entries must have title and contents" 

def test_readin_time_with_two_wpm_and_four_words ():
    diary_entry = DiaryEntry("My Title", "one two three four")
    result = diary_entry.reading_time (2)
    assert result == 2

def test_readin_time_with_two_wpm_and_three_words ():
    diary_entry = DiaryEntry("My Title", "one two three")
    result = diary_entry.reading_time (2)
    assert result == 2

def test_reading_time_wpm_of_zero ():
    diary_entry = DiaryEntry ("My Title","one two three")
    with pytest.raises(Exception) as err:
        diary_entry.reading_time(0)
    assert str(err.value) == "Cannot calculate reading time with wpm of 0"

def test_errors_on_empty_title(): 
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    assert str(err.value) == "Diary entries must have title and contents" 

def test_errors_on_empty_contents(): 
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    assert str(err.value) == "Diary entries must have title and contents" 

# def test_reading_chunk_with_two_wpm_and_two_minutes():
#     diary_entry = DiaryEntry("My Title", "one two three four five six")
#     result = diary_entry.reading_chunk(2, 2)
#     assert result == "one two three four"

# def test_reading_chunk_with_two_wpm_and_one_minute_called_multiple_times ():
#     diary_entry = DiaryEntry ("My Title", "one two three four five six")
#     assert diary_entry.reading_chunk(2, 1) == "one two" 
#     assert diary_entry.reading_chunk(1, 1) == "three"
#     assert diary_entry.reading_chunk(2, 1) == "four five"

    
    