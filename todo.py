# To-Do List (Day 3) - Step 1 

import json, os
FILE = "todo.json"

def load_tasks():
    global tasks
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            tasks = json.load(f)
    else:
        tasks = []

def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def menu():
    print("== TO-DO LIST ==")
    print("1) List Task")
    print("2) Add Task")
    print("3) Complete task")
    print("4) Delete Task")
    print("5) Quit")

def main():
    while True:
        menu()
        choice = input("Choose: ").strip()
        if choice == "5":
            print("Bye!")
            break
        else:
            print("Not implemented yet.\n")

# TO-DO List Step 2 (list tasks)

tasks = [] # we'll store dicts later; for now just strings is fine 

def list_task():
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    print("\nYour Tasks")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")
    print()

def menu():
    print("== TO-DO LIST ==")
    print("1) List tasks")
    print("2) Add task")
    print("3) Complete task")
    print("4) Delete task")
    print("5) Quit")

def main():
    while True:
        menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            list_task()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Not implemented yet.\n")

#To-Do List Step 3 (add tasks)

tasks = []

def list_tasks():
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")
    print()

def add_task():
    title = input("New task: ").strip()
    if title:
        tasks.append(title)
        print("Added!\n")
    else:
        print("Empty task ignored.\n")

def menu():
    print("== TO-DO LIST ==")
    print("1) List tasks")
    print("2) Add task")
    print("3) Complete task")
    print("4) Delete task")
    print("5) Quit")

def main():
    while True:
        menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Not implemented yet.\n")

# To-Do List (Step 4) — mark tasks complete

# Store each task as a dict so we can track completion
tasks = []  # e.g. {"title": "Do homework", "done": False}

def list_tasks():
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "[x]" if t["done"] else "[ ]"
        print(f"{i}. {status} {t['title']}")
    print()

def add_task():
    title = input("New task: ").strip()
    if not title:
        print("Empty task ignored.\n")
        return
    tasks.append({"title": title, "done": False})
    print("Added!\n")

def complete_task():
    if not tasks:
        print("Nothing to complete.\n")
        return
    list_tasks()
    raw = input("Complete which #? ").strip()
    if not raw.isdigit():
        print("Enter a number.\n"); return
    idx = int(raw)
    if 1 <= idx <= len(tasks):
        tasks[idx-1]["done"] = True
        print(f"Completed: {tasks[idx-1]['title']}\n")
    else:
        print("Invalid number.\n")

def delete_task():
    if not tasks:
        print("Nothing to delete.\n")
        return
    list_tasks()
    raw = input("Delete which #? ").strip()
    if not raw.isdigit():
        print("Enter a number.\n"); return
    idx = int(raw)
    if 1 <= idx <= len(tasks):
        removed = tasks.pop(idx-1)
        print(f"Deleted: {removed['title']}\n")
    else:
        print("Invalid number.\n")

def menu():
    print("== TO-DO LIST ==")
    print("1) List tasks")
    print("2) Add task")
    print("3) Complete task")
    print("4) Delete task")
    print("5) Quit")

def main():
    while True:
        menu()
        choice = input("Choose: ").strip()
        if choice == "1":
            list_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Not implemented yet.\n")

if __name__ == "__main__":
    load_tasks()
    main()


