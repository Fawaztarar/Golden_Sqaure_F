ls


def test_initially_has_no_tasks():
    tracker = TodoList ()
    tracker.incomplete ()



def test_add_todo_reflected_in_tasks():
    tracker = TodoList()
    new_todo = Todo("COMPLETE PHASE TWO")
    tracker.add(new_todo)
    assert tracker.incomplete() == [new_todo]




def test_add_multiple_tasks_reflected_in_tasks():
    tracker = TodoList ()
    new_todo = Todo("COMPLETE PHASE TWO")
    new_todo2 = Todo("COMPLETE PHASE THREE")
    tracker.add(new_todo)
    tracker.add(new_todo2)
    assert tracker.incomplete () == [new_todo, new_todo2]



def test_incomplete_and_complete():
    todo_list = TodoList()
    todo1 = Todo("COMPLETE PHASE 4")
    todo2 = Todo("COMPLETE PHASE 1")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo2.mark_complete()
    assert todo_list.incomplete() == [todo1]
    assert todo_list.complete() == [todo2]


def test_give_up():
    todo_list = TodoList()
    todo_list.add(Todo("CHAPTER 08"))
    todo_list.add(Todo("CHAPTER 09"))
    todo_list.give_up()
    assert all(todo.complete for todo in todo_list.todos)