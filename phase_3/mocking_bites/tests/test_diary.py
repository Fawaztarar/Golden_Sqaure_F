from lib.diary import Diary


def test_can_read_contents ():
    diary = Diary ("My Contents")
    assert diary.read () == "My Contents"