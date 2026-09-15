class TodoList:

    def __init__(self):
        self.tasks = []

    def add_task(self, *task_names):

        for task in task_names:

            self.tasks.append({
                "task": task,
                "completed": False
            })

        print("tasks added successfully!")

    def view_tasks(self):

        if not self.tasks:
            print("No tasks available.")

        else:
            print("\n========TODO LIST========")

            i = 1

            for task in self.tasks:

                if task["completed"] == True:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"{i}. {task['task']} - {status}")

                i = i + 1

    def complete_task(self):

        self.view_tasks()

        if self.tasks:

            try:
                task_number = int(input("Enter task number to complete: "))

                if 1 <= task_number <= len(self.tasks):

                    self.tasks[task_number - 1]["completed"] = True

                    print("Task marked as completed!")

                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    def update_task(self):

        self.view_tasks()

        if self.tasks:

            try:
                task_number = int(input("Enter task number to update: "))

                if 1 <= task_number <= len(self.tasks):

                    new_task = input("Enter new task name: ")

                    self.tasks[task_number - 1]["task"] = new_task

                    print("Task updated successfully!")

                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

    def remove_task(self):

        self.view_tasks()

        if self.tasks:

            try:
                task_number = int(input("Enter task number to remove: "))

                if 1 <= task_number <= len(self.tasks):

                    removed_task = self.tasks.pop(task_number - 1)

                    print(f"{removed_task['task']} removed successfully!")

                else:
                    print("Invalid task number!")

            except ValueError:
                print("Please enter a valid number!")

todo = TodoList()

todo.add_task("study_time","play_time","Dinner_time","sleep_time")

while True:

    print("\n******TODO LIST**********")

    print("1. View Tasks")
    print("2. Complete Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

    option = input("Enter your Choice: ")


    if option== "1":

        todo.view_tasks()


    elif option == "2":

        todo.complete_task()


    elif option == "3":

        todo.update_task()


    elif option == "4":

        todo.remove_task()


    elif option == "5":

        print("Thank you for using TodoList!")

        break
    else:

        print("Invalid choice! Please try again.")




     