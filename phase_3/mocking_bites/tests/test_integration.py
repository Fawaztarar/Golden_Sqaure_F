import pytest
from lib.diary import Diary 
from lib.secret_diary import SecretDiary

def test_locked_diaries_can_not_be_read():
    diary = Diary ("My Contents")
    secret_diary = SecretDiary (diary)
    with pytest.raises (Exception) as err:
        secret_diary. read ()
    assert str(err.value) == "Go away!"



def test_relocked_diaries_can_not_be_read():
    diary = Diary ("My Contents")
    secret_diary = SecretDiary (diary)
    secret_diary.unlock()
    secret_diary.lock()
    with pytest.raises (Exception) as err:
        secret_diary. read ()
    assert str(err.value) == "Go away!"