def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

tasks = []

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        if not tasks:
            print("\nYour to-do list is empty!")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    elif choice == '2':
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print(f"'{new_task}' added!")
    elif choice == '3':
    
        pass
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")