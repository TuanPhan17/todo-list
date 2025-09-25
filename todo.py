# To-Do List (Day 3) - Step 1 

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

if __name__ == "__main__":
    main()
