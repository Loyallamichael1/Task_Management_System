
import csv
#I need to use this "csv" thing to help save our tasks in a file later.


tasks = []
#I got to make an empty list called tasks to keep all the tasks safe.

#Now I got to make a function to display the main menu
def display_menu():
    print("\n--- Task Management System ---")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Search Task")
    print("4. Export Tasks")
    print("5. Exit")
#This shows the menu so the user knows what choices they can make (like add a task, delete one, or leave).

#I got to make this function to run the system
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            search_task()
        elif choice == "4":
            export_tasks()
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid. Please try again.")
#This part keeps showing the menu until the user chooses to exit. It does what the user asks like adding a task or searching for one.

#Now I got to make a function to add a task
def add_task():
    print("\n--- Add a New Task ---")
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")
    status = input("Enter the task status (Incomplete/Completed): ")
    #We need the title to know what the task is, the description to explain it, 
    #the due date to remember when it's due, and the status to see if it's finished or not.


#Now I got to create a task dictionary
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": status
    }

#Now I got to add the task to the tasks list
    tasks.append(task)
    print(f"Task '{title}' added successfully!")

#This part lets the user add a new task. They can type the name, description, when it’s due, and whether it's done or not. 
#Then we save it in the list of tasks.

#Now I got to make a function to delete a task
def delete_task():
    print("\n--- Delete a Task ---")
    choice = input("Search by (1) Title or (2) Due Date: ")

    if choice == "1":
        title = input("Enter the task title to delete: ")
        task_found = False
        for task in tasks:
            if task["title"] == title:
                tasks.remove(task)
                print(f"Task '{title}' deleted successfully!")
                task_found = True
                break
        if not task_found:
            print("Task not found.")
    elif choice == "2":
        due_date = input("Enter the task due date to delete: ")
        task_found = False
        for task in tasks:
            if task["due_date"] == due_date:
                tasks.remove(task)
                print(f"Task due on {due_date} deleted successfully!")
                task_found = True
                break
        if not task_found:
            print("Task not found.")
    else:
        print("Invalid choice. Please choose (1) or (2).")
 #This part helps the user delete a task. They can pick if they want to delete by title or by due date. 
 #If the task is found, it gets deleted.

# Function to search for a task
def search_task():
    print("\n--- Search for a Task ---")
    choice = input("Search by (1) Title or (2) Due Date: ")

    if choice == "1":
        title = input("Enter the task title to search: ")
        task_found = False
        for task in tasks:
            if task["title"] == title:
                print(f"Task found: {task}")
                task_found = True
                break
        if not task_found:
            print("Task not found.")
    elif choice == "2":
        due_date = input("Enter the task due date to search: ")
        task_found = False
        for task in tasks:
            if task["due_date"] == due_date:
                print(f"Task found: {task}")
                task_found = True
                break
        if not task_found:
            print("Task not found.")
    else:
        print("Invalid choice. Please choose (1) or (2).")
#This lets the user search for a task. They can search by title or by the due date. 
#If the task is found, it shows the details, and if not, it says the task isn’t there.

#Now I got to make a function to export tasks to a CSV file
def export_tasks():
    print("\n--- Export Tasks ---")
    filename = input("Enter the filename to export (e.g., tasks.csv): ")

    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["title", "description", "due_date", "status"])
            writer.writeheader()  #I got to write the header row
            writer.writerows(tasks)  #I got to write a task data
        print(f"Tasks exported successfully to {filename}")
    except Exception as e:
        print(f"Error exporting tasks: {e}")
#This part saves the tasks to a file in CSV format. 
#The user gives the file name, and the tasks are written into it. If there’s an error, it tells the user.

#Now I got to run the system
if __name__ == "__main__":
    main()
#This starts the program when you run it.