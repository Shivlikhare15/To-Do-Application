#Create an empty list to store the tasks and their status
todo_list = []



#Function to add a new task
def add_task():
    task = input("Enter a task:")
    todo_list.append({"Task":task,"Status":"pending"})
    print("New Task Added Successfully!\n")

#Function to view all tasks
def view_task():
    print("your todo list:")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")   


# Function to remove a task
def remove_task():
    if len(todo_list) == 0:
        print("List is Empty \n")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove:"))-1
            if 0 <= search_index < len(todo_list):
                remove_task = todo_list.pop(search_index)
                print(f"Task removed:{remove_task["Task"]}")
            else:
                print("Invalid task Number.") 
        except ValueError:        
            print("Please enter a valid number")


#Function to mark a task as complete
def mark_done():
    if len(todo_list) == 0:
        print("List is Empty \n")
    else:
        try:
            search_index = int(input("Enter the task number that you want to mark as complete:"))-1
            if 0 <= search_index < len(todo_list):
               todo_list[search_index]['Status']='done'
               print(f"Task {todo_list[search_index]['Task']} has been mark done.")
            else:
                print("Invalid task Number.") 
        except ValueError:        
            print("Please enter a valid number")        


#Function to Display the menu
def menu():
    while (True):
        print("***** To-Do List Menu *****")
        print("1.Add a new task")
        print("2.View all tasks")
        print("3.Remove a task")
        print("4.Mark a task as completed")
        print("5.Exit") 



        choice = input("Enter your choice:")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            print("Exiting the program...")
            exit()
        else:
            print("Invalid choice! please try again")


menu()            