import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        save_tasks([])
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        save_tasks([])
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_desc):
    tasks = load_tasks()
    tasks.append({"task": task_desc, "completed": False})
    save_tasks(tasks)
    print(f'Added task: "{task_desc}"')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['task']} [{status}]")

def complete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print(f'Task {task_number} marked as completed! ✅')
    else:
        print("Invalid task number.")

def delete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Deleted task: "{removed["task"]}"')
    else:
        print("Invalid task number.")

def main():
    while True:
        command = input("\nEnter a command (add, list, complete, delete, exit): ").strip().lower()
        
        if command.startswith("add "):
            task_desc = command[4:].strip()
            add_task(task_desc)

        elif command == "list":
            list_tasks()

        elif command.startswith("complete "):
            try:
                task_number = int(command.split()[1])
                complete_task(task_number)
            except ValueError:
                print("Invalid task number format.")

        elif command.startswith("delete "):
            try:
                task_number = int(command.split()[1])
                delete_task(task_number)
            except ValueError:
                print("Invalid task number format.")

        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid command. Try: add, list, complete, delete, exit.")

if __name__ == "__main__":
    main()
