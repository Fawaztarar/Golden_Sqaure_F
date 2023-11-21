from lib.task_list import *
from lib.task import *

def test_adds_and_lists_incomplete_tasks () :
    task_list = TaskList()
    task_1 = Task ("Walk the dog")
    task_2 = Task("Walk the cat")
    task_3 = Task("Walk the frog")
    task_list.add(task_1) 
    task_list.add(task_2) 
    task_list.add(task_3)
    assert task_list.all_incomplete () == [task_1, task_2, task_3]