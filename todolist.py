def main():
    #To hold all the tasks
    tasks= []

    while True:
        print("\n====== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        #Take Input from user
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print()
            no_of_tasks = int(input("How many task you want to add:"))

            #Loop to enter the preffered no.of tasks
            for i in range(no_of_tasks):
                task = input("Enter the Task Name: ")
                tasks.append({"task":task, "done":False})
                print("Task added!")

        elif choice == 2:
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == 3:
            task_index = int(input("Enter the task number to mark as done: "))
            if 0 <= task_index < len(tasks):
                tasks[task_index]['done'] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == 4:
            print("Exiting the To-Do List.")
            break
        else:
            print("Invalid choice. Plese try again.") 

if __name__ == "__main__":
    main()



