def display_menu():
    print("""
===== TO‑DO LIST =====
1. Add Task
2. Show Tasks
3. Mark Task as Done
4. Delete Task
5. Exit
""")

def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("Task added!")
    else:
        print("Cannot add an empty task.")

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, 1):
            status = "Done" if t["done"] else "Not done"
            print(f"{i}. {t['task']} - {status}")

def mark_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    choice = input("Task number to mark as done: ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Marked as done:", tasks[idx]["task"])
        else:
            print("Invalid task number.")
    else:
        print("Enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    choice = input("Task number to delete: ").strip()
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print("Removed:", removed["task"])
        else:
            print("Invalid task number.")
    else:
        print("Enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1‑5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print(" Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

