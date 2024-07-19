class TaskManager:

    def __init__(self): 
        self.tasks = {} # {id,object}
        

    def display_task_counts(self):
        task_count = len(self.tasks)
        print (f"Total Task Count:{task_count}")

        completed_count = sum(1 for task in self.tasks.values() if task.get('completed', True))
        print(f"Completed Count: {completed_count}")
        print() #for clarity

    def display_task_details(self):
            for task_id, task_info in self.tasks.items():
                print(f"Task ID: {task_id}")
                for key, value in task_info.items():
                    print(f"{key.capitalize()}: {value}")
            
