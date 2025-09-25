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

if __name__ == "__main__":
    main()