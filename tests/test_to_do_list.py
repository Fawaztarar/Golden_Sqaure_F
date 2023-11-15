from lib.to_do_list import *


def test_to_do_task():
    result = to_do_task("#TODO have appoitment on friday ")
    assert result is True

def test_to_do_task_two():
    result = to_do_task_two("#TODO have to record it")
    assert result == True

