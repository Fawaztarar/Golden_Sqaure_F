# **Immplement the following user stories in your project. Both of these will be within a single class.



#DESCRIBE PROBLEM


#As a user
# So that I can keep track of my tasks
# I want a program that I can add todo tasks to and see a list of them.
# As a user
# So that I can focus on tasks to complete
# I want to mark tasks as complete and have them disappear from the list.


# DESIGN CLASS INTERFACE


# add, list, mark complete, removal of complete task
class todoBook:
    def __init__(self):
        self._tasks = []  

    def add_task(self, task):
        self._tasks.append(task)

    def list_incomplete(self):
        return self._tasks
    

    def mark_complete (self, index):
        if index < 0:
            raise Exception ("No such task to mark complete")
        del self._tasks[index]


    #EXAMPLE OF TESTS

    # 1 EMPTY TO DO book (EMPTY STRING)

    

    # Add task to do book

    # list all todo tasks


    # Mark completed task

    # Delelte completed task from list

    # show updated list










