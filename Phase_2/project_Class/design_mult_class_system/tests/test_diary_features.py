from lib import diary_entry
from lib.diary import *
from lib.diary_entry import *
from lib.diary import Diary 
from lib.diary_entry import DiaryEntry


def test_adds_and_lists_entries ():
    diary = Diary ()
    entry_1 = DiaryEntry ("My Title 1", "My Contents 1")
    entry_2 = DiaryEntry ("My Title 2", "My Contents 2")
    entry_3 = DiaryEntry ("My Title 3", "My Contents 3")
    diary.add(entry_1)
    diary.add(entry_2) 
    diary.add(entry_3)
    assert diary.all () == [entry_1, entry_2, entry_3]