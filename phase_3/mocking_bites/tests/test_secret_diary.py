import pytest
from unittest.mock import Mock 
from lib.secret_diary import SecretDiary


def test_locked_diaries_can_not_be_read() :
    diary = Mock ()
    secret_diary = SecretDiary (diary)
    with pytest.raises (Exception) as err:
        secret_diary. read ()
    assert str(err.value) == "Go away!"


def test_unlocked_diaries_can_be_read():
    diary = Mock()
    diary.read. return_value = "Cool Contents"
    secret_diary = SecretDiary (diary)
    secret_diary.unlock()
    assert secret_diary.read() == "Cool Contents"
    diary.read.assert_called ()