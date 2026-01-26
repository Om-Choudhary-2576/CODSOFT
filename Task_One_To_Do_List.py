# A simple To-Do List Manager
tasks = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        if not tasks:
            print("\nYour list is empty.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    
    elif choice == '2':
        new_task = input("Enter the task: ")
        tasks.append(new_task)
        print("Task added!")
    
    elif choice == '3':
        if tasks:
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                   
                    task_to_delete = tasks[task_num - 1]
                    
                    tasks.remove(task_to_delete)
                    print(f"Successfully removed: {task_to_delete}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Nothing to remove.")
            
    elif choice == '4':
        print("Exiting....")
        break
    else:
        print("Invalid choice, try again.")