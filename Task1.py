import json
from datetime import datetime

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to display menu
def display_menu():
    print("\n==== TO-DO LIST ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

# Function to add task
def add_task(tasks):
    description = input("Enter task description: ")
    due_date = input("Enter due date (DD-MM-YYYY): ")
    tasks.append({"description": description, "due_date": due_date})
    print("Task added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task['description']} (Due: {task['due_date']})")
    else:
        print("No tasks found.")

# Function to update task
def update_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter task number to update: ")) - 1
    description = input("Enter new description (leave blank to keep current): ")
    due_date = input("Enter new due date (DD-MM-2024) (leave blank to keep current): ")
    if description:
        tasks[task_index]['description'] = description
    if due_date:
        tasks[task_index]['due_date'] = due_date
    print("Task updated successfully!")

# Function to delete task
def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter task number to delete: ")) - 1
    del tasks[task_index]
    print("Task deleted successfully!")

def main():
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
