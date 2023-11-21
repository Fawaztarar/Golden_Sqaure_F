class TaskList():
    def init_ (self):
        self._tasks = []
        
    def add(self, task):
        self. _tasks.append (task)

    def all_incomplete(self):
        return self._tasks