def add_task():
    global task_id_counter  # To modify the global counter
    
    # Get task details from the user
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    
    # Generate a unique task ID
    task_id = task_id_counter
    task_id_counter += 1
    
    # Create a dictionary to represent the task
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "due_date": due_date
    }
    
    # Add the task to the list of tasks
    tasks.append(task)
    print(f"Task added successfully with ID {task_id}")

def view_tasks():
    # TODO: Implement task viewing logic
    pass

def edit_task():
    # TODO: Implement task editing logic
    pass

def delete_task():
    # TODO: Implement task deletion logic
    pass

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
