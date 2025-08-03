# tasks = []
# done = []

# def add_task():
#     task = input("Enter task:").lower()
#     if task in tasks:
#         print("Already available")
#     else:
#         tasks.append(task)


# def remove_task():
#     task = input("Enter the task to be removed:").lower()
#     if task in tasks:
#         tasks.remove(task)
#     elif task in done:
#         done.remove(task)
#     else:
#         print("Task not found")

# def view_tasks():
#     resp = int(input("You want to view pending tasks or completed tasks ??(1:pending,2:completed)"))
#     if resp!=2:
#         print(tasks)
#     else:
#         print(done)

# def tasks_done():
#     resp = input("Which task completed ?").lower()
#     if resp not in tasks:
#         print("No such task found")
#     else:
#         if resp not in done:
#             done.append(resp)
#             tasks.remove(resp)

import json
import os

TODO_FILE = "todo.json"

# Function 1: Load tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w") as f:
            json.dump({"tasks": [], "done": []}, f)
    
    with open(TODO_FILE, "r") as f:
        return json.load(f)

# Function 2: Save tasks to file
def save_tasks(data):
    with open(TODO_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Function 3: Add a task
def add_task():
    data = load_tasks()
    task = input("Enter a new task: ").lower()
    if task in data["tasks"]:
        print("Task already exists.")
    else:
        data["tasks"].append(task)
        save_tasks(data)
        print("Task added.")

# Function 4: Remove a task
def remove_task():
    data = load_tasks()
    task = input("Enter the task to remove: ").lower()
    if task in data["tasks"]:
        data["tasks"].remove(task)
    elif task in data["done"]:
        data["done"].remove(task)
    else:
        print("Task not found.")
        return
    save_tasks(data)
    print("Task removed.")

# Function 5: View tasks
def view_tasks():
    data = load_tasks()
    choice = input("View (1) Pending or (2) Completed tasks? ")
    if choice == "1":
        print("\nPending Tasks:")
        for i, task in enumerate(data["tasks"], 1):
            print(f"{i}. {task}")
    elif choice == "2":
        print("\nCompleted Tasks:")
        for i, task in enumerate(data["done"], 1):
            print(f"{i}. {task}")
    else:
        print("Invalid choice.")

# Function 6: Mark task as done
def mark_done():
    data = load_tasks()
    task = input("Which task is done? ").lower()
    if task in data["tasks"]:
        data["tasks"].remove(task)
        data["done"].append(task)
        save_tasks(data)
        print("Marked as done.")
    else:
        print("Task not found in pending list.")
