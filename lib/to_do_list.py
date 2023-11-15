def to_do_task(task):
    to_do_list = ["#TODO"]
    return any(todo in task for todo in to_do_list)

def to_do_task_two(task):
    return task[:4]in "#TODO"