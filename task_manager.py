class TaskManager:

    def __init__(self):
        self.tasks = {1: "taks1", 2: "task2"}  # {id,object}



    def display_tasks(self):
        for value in self.tasks.values():
            print(value)




task_manager = TaskManager()



task_manager.display_tasks()