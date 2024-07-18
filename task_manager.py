class TaskManager:

    def __init__(self): 
        self.tasks = {
            1: {"title": "Task 1", "description": "Description of task 1", "category": "Front-end"},
            2: {"title": "Task 2", "description": "Description of task 2", "category": None}
        } # test amacli dummy tasks 
        

    def display_tasks(self):
        task_count = len(self.tasks)
        print (f"Total Task Count:{task_count}")

        for task_id, task_info in self.tasks.items():
            print(f"Task ID: {task_id}")
            for key, value in task_info.items():
                    print(f"{key.capitalize()}: {value}")

task_manager = TaskManager()

# fonksiyonlari konsola bu sekilde cagirabilirsiniz.
task_manager.display_tasks()