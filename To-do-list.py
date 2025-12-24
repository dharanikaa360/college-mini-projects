# Simple To-Do List
tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == '3':
        print("Exiting To-Do List.")
        break
    else:
        print("Invalid choice, try again.")
