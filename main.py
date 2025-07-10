class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        if not any(t['task'] == task_name for t in self.tasks):
            self.tasks.append({"task": task_name, "status": "Pending"})
            print(f"Task ''{task_name}'' added.")
        else:
            print(f"Task ''{task_name}'' already exists.")

    def list_tasks(self):
        if not self.tasks:
            return "The to-do list is empty."
        
        output = "Tasks:\n"
        for task in self.tasks:
            output += f"- {task['task']}\n"
        return output

    def mark_task_as_completed(self, task_name):
        for task in self.tasks:
            if task['task'] == task_name:
                task['status'] = "Completed"
                print(f"Task ''{task_name}'' marked as completed.")
                return
        print(f"Task ''{task_name}'' not found.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared.")

    def delete_task(self, task_name):
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t['task'] != task_name]
        if len(self.tasks) < initial_count:
            print(f"Task ''{task_name}'' deleted.")
        else:
            print(f"Task ''{task_name}'' not found.")

    def edit_task(self, old_task_name, new_task_name):
        for task in self.tasks:
            if task['task'] == old_task_name:
                task['task'] = new_task_name
                print(f"Task ''{old_task_name}'' edited to ''{new_task_name}''")
                return
        print(f"Task ''{old_task_name}'' not found.")

if __name__ == '__main__':
    todo = ToDoList()
    print("--- To-Do List Manager ---")

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Edit task")
        print("6. Clear all tasks")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task description: ")
            todo.add_task(task)
        elif choice == '2':
            print(todo.list_tasks())
        elif choice == '3':
            task = input("Enter the task to mark as completed: ")
            todo.mark_task_as_completed(task)
        elif choice == '4':
            task = input("Enter the task to delete: ")
            todo.delete_task(task)
        elif choice == '5':
            old_task = input("Enter the task to edit: ")
            new_task = input("Enter the new task description: ")
            todo.edit_task(old_task, new_task)
        elif choice == '6':
            todo.clear_tasks()
        elif choice == '7':
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")