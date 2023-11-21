import pytest
from lib.todo_book import *

# empty diary or empty list

def test_initially_has_no_tasks():
    tracker = todoBook ()
    tracker.list_incomplete ()



def test_add_task_reflected_in_tasks():
    tracker = todoBook()
    tracker.add_task("COMPLETE PHASE TWO")
    assert tracker.list_incomplete() == ["COMPLETE PHASE TWO"]


def test_add_multiple_tasks():
    tracker = todoBook ()
    tracker.add_task("COMPLETE PHASE TWO")
    tracker.add_task("GO SHOPPING")
    tracker.add_task("MEET UP FRIEND")
    assert tracker.list_incomplete () == ["COMPLETE PHASE TWO",
            "GO SHOPPING", "MEET UP FRIEND"]

def test_marks_task_complete():
    tracker = todoBook ()
    tracker.add_task("COMPLETE PHASE TWO")
    tracker.add_task("GO SHOPPING")
    tracker.add_task("MEET UP FRIEND")
    tracker.mark_complete(1)
    assert tracker.list_incomplete () == ["COMPLETE PHASE TWO", "MEET UP FRIEND"]


def test_marks_task_complete_easy_task():
    tracker = todoBook ()
    tracker.add_task("COMPLETE PHASE TWO")
    with pytest.raises(Exception) as err:
        tracker.mark_complete(-1)
    assert str(err.value) == "No such task to mark complete"
    assert tracker.list_incomplete() == ["COMPLETE PHASE TWO"]

