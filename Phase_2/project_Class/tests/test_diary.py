import pytest
from lib.diary import *

def test_initially_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []



def test_initially_reading_time_raises_error():
    diary = Diary ()
    with pytest.raises (Exception) as err:
        diary.reading_time (2)
    assert str(err.value) == "No entries added yet"