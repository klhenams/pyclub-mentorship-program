# Project: Task Manager

# Description: Create a command-line task manager that allows users to add, view, edit, and delete tasks.

tasks = []
task_id_counter = 1

#Display Menu
def display_menu():
    print('Task Manager Menu:')
    print('1. Add task')
    print('2. View task')
    print('3. Edit task')
    print('4. Delete task')
    
def add_task():
    global task_id_counter
    title = input('Enter task title:')
    description = input('Enter task description:')
    due_date = input('Enter task due date:')
    pass

    task = dict()
    task['id'] = task_id_counter
    task['title'] = title
    task['description'] = description
    task['due date'] = due_date

    tasks.append(task)
    task_id_counter += 1
    print('Task Added Successfully!')


def view_tasks():
    print('Task list:')
    for task in tasks:
        print(f"ID:{task['id']}, Title:{task['title']}, Description:{task['description']}, Due Date: {task['due date']}")


def edit_task():
    try:
        task_id = input('Enter the ID of the task you want to edit:')
        task = next(task for task in tasks if task['id']==task_id)

        title = input('Enter new title:')
        description = input('Enter new description:')
        due_date =input('Enter new due date:')

        task['title'] = title
        task['description'] = description
        task['due date'] = due_date

        print('Task Edited Successfully')
    except  StopIteration:
        print('Task not found') 
    except ValueError:
        print('Invalid Input. Enter a valid task ID')


def delete_task():
    try:
        task_id = input('Enter the name of the ID you want to delete:')
        tasks[:] = [task for task in tasks if task['id'] != task_id]
        print('Task deleted successfully!')
    except ValueError:
        print('Invalid input. Please enter a valid task ID')
        

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