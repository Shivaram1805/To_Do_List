def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter task priority (high/medium/low): ").lower()
    while priority not in ['high', 'medium', 'low']:
        print("Invalid priority! Please enter high, medium, or low.")
        priority = input("Enter task priority (high/medium/low): ").lower()
    due_date = input("Enter due date: ")
    tasks.append({"name": task_name, "priority": priority, "due_date": due_date, "completed": False})
    print("Task added successfully!")

def remove_task(tasks):
    task_name = input("Enter task name to remove: ")
    for i in tasks:
        if i["name"] == task_name:
            tasks.remove(i)
            print("Task removed successfully!")
            return
    print("Task not found.")

def mark_task_completed(tasks):
    task_name = input("Enter task name to mark as completed: ")
    for i in tasks:
        if i["name"] == task_name:
            i["completed"] = True
            print("Task marked as completed!")
            return
    print("Task not found.")

def display_tasks(tasks):
    print("TO-DO LIST:")
    for i, j in enumerate(tasks, start=1):
        print(i, j['name'], "- Priority:", j['priority'].capitalize(), ", Due Date:", j['due_date'], ", Completed:", j['completed'])

tasks = []
while True:
    print("\n------- TO-DO LIST MENU -------")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. Display Tasks")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        remove_task(tasks)
    elif choice == "3":
        mark_task_completed(tasks)
    elif choice == "4":
        display_tasks(tasks)
    elif choice == "5":
        print("Have A Nice Day...")
        break
    else:
        print("Invalid choice. Please try again.")