import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.\n")
    else:
        print("\nYour Tasks:\n")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()


def add_task(tasks):
    task = input("Enter task: ")

    if task.strip() == "":
        print("Task cannot be empty.\n")
    else:
        tasks.append(task)
        print("Task added successfully.\n")


def delete_task(tasks):
    show_tasks(tasks)

    if len(tasks) == 0:
        return

    try:
        index = int(input("Enter task number to delete: "))

        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(index - 1)
            print(f'"{removed_task}" deleted successfully.\n')
        else:
            print("Invalid task number.\n")

    except ValueError:
        print("Please enter a valid number.\n")


def main():
    tasks = load_tasks()

    while True:
        print("===== TO-DO LIST =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        show_tasks(tasks)

        if choice == "1":
            #  show_tasks(tasks)
            pass

        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)

        elif choice == "4":
            save_tasks(tasks)
            print("\nExiting To-Do App...")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()