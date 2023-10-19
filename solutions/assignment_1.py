# Project: Task Manager

# Description: Create a command-line task manager that allows users to add, view, edit, and delete tasks.

# Key Concepts to Learn:

# Data Types (strings, lists, dictionaries)
# Functions
# Flow Control Statements (if, while, for)
# User Input and Output
# Error Handling (try...except)
# Project Steps:

# Initialization:

# Initialize an empty list to store tasks.
# Define a dictionary to map task IDs to task details.
# Menu System:

# Create a menu system with options like "Add Task," "View Tasks," "Edit Task," "Delete Task," and "Exit."
# Add Task:

# Allow users to input task details (e.g., title, description, due date).
# Generate a unique task ID.
# Create a dictionary to represent the task and add it to the list of tasks.
# View Tasks:

# Display a list of tasks with their details (ID, title, description, due date).
# Allow users to filter tasks (e.g., view all tasks, view tasks by due date, view tasks by status, etc.).
# Edit Task:

# Prompt the user for the task ID they want to edit.
# Allow them to modify task details (title, description, due date).
# Update the task in the list.
# Delete Task:

# Prompt the user for the task ID they want to delete.
# Remove the task from the list.
# Error Handling:

# Implement error handling to deal with invalid inputs or non-existent tasks.
# Save and Load Data (Optional):

# Implement functionality to save tasks to a file (e.g., JSON) and load them when the program starts.
# Exit:

# Provide an option to exit the program.
# User Interface:

# Format the user interface to make it user-friendly.
# Testing:

# Test your program thoroughly to ensure it works as expected.

# Sample Code Outline:

# Here's a simplified code outline to get you started. You can expand and refine it as you work on the project:


tasks = []
task_id_counter = 1

def add_task():
    # TODO: Implement task addition logic
    global task_id_counter
    title = input("Enter the task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date of task: ")

    task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "due date": due_date,
    }
    tasks.append(task)
    task_id_counter += 1
    print("Task added successfully")

def view_tasks():
    # TODO: Implement task viewing logic
    if not tasks:
        print("No tasks available. Add a task")
        return
    print("Available Tasks")
    for task in tasks:
       print(f"Task ID: {task['id']}") 
       print(f"Title: {task['title']}")
       print(f"Description: {task['description']}")
       print(f"Due Date: {task['due date']}")
       print()

def edit_task():
    # TODO: Implement task editing logic
    view_tasks()
    task_id = int(input("Enter the task ID you want to edit: "))
    found = False

    for task in tasks:
        if task['id'] == task_id:
            found = True
            title = input("Enter updated task title (press Enter to keep the same): ")
            description = input("Enter updated task description (press Enter to keep the same): ")
            due_date = input("Enter updated due date (press Enter to keep the same): ")

            # Update task details
            task['title'] = title if title else task['title']
            task['description'] = description if description else task['description']
            task['due_date'] = due_date if due_date else task['due_date']
            print("Task updated successfully.")
            break

    if not found:
        print("Task not found. Please enter a valid task ID.")

def delete_task():
    # TODO: Implement task deletion logic
    view_tasks()
    task_id = int(input("Enter the task ID you want to delete: "))
    found = False

    for task in tasks:
        if task['id'] == task_id:
            found = True
            tasks.remove(task)
            print("Task deleted successfully.")
            break

    if not found:
        print("Task not found. Please enter a valid task ID.")

def main():
    while True:
        print("Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
