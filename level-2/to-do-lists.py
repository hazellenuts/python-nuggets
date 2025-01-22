import json
import os

TODO_FILE = "python-nuggets/level-2/todo.json"

def load_task():
    try:
        with open(TODO_FILE, "r") as file:
            tasks = json.load(file)
            
    except FileNotFoundError:
        tasks = []
        print("file not found")
    return tasks

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start = 1):
            status = "✅" if task["status"] == "completed" else "⬜"
            print(f"{status} {i}. {task['task']}")

def add_task(tasks):
    desc = input("Enter the task description:")
    new_task = {
        "task": desc,
        "status": "pending"
    }
    tasks.append(new_task)
    print("Task added successfully!")

def mark_completed(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <=len(tasks):
            tasks[task_num-1]["status"] = "completed"
            print(f"Task {task_num} marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num-1)
            print(f"Task '{deleted_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent = 4)

def main():
    print("Let's get things done!")
    tasks = load_task()

    while True:
        display_tasks(tasks)
        print("""
1. Add a task
2. Mark a task as completed
3. Delete a task
4. Exit
""")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            mark_completed(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("saving tasks to file...")
            print("Stay Productive! —hazellenuts")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()