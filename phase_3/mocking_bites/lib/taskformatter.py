class TaskFormatter:
    def __init__(self, task):
        self.task = task

    def format(self):
        status = "[x]" if self.task.is_complete() else "[ ]"
        return f"- {status} {self.task.title}"