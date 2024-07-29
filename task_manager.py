from task import Task
from datetime import datetime


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def filter_tasks_by_due_date(self, due_date_str):
        """Return tasks due on the specified date."""
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        return [task for task in self.tasks if task.due_date == due_date]
