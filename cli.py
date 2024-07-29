from task_manager import TaskManager


class CLI:
    def __init__(self, task_manager, user_manager):
        self.task_manager = task_manager
        self.user_manager = user_manager


def main():
    task_manager = TaskManager()

    while True:
        command = input("Enter command (add/filter/exit): ").strip().lower()

        if command == 'add':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")

            task = task_manager.add_task(title, description)
            task.set_due_date(due_date)
            print(f"Task '{title}' added with due date {due_date}.")

        elif command == 'filter':
            due_date = input("Enter due date to filter tasks (YYYY-MM-DD): ")
            tasks = task_manager.filter_tasks_by_due_date(due_date)

            for task in tasks:
                print(f"{task.title}: {task.description} (Due: {task.get_due_date()})")

        elif command == 'exit':
            break

        else:
            print("Invalid command. Please enter 'add', 'filter', or 'exit'.")


if __name__ == "__main__":
    main()
