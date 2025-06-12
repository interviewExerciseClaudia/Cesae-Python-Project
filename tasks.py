#=====global variables===========
user_credentials = {}
all_users_tasks = {}
user_tasks = {}
username = ""
password = ""

#=====Authentication===========

def get_credentials():
    all_credentials = {
        "claudia" : "passwd1",
        "felippe" : "passwd2"
    }
    return all_credentials

def authenticate():
    username = input("Username: ")
    password = input("Password: ")

    user_credentials = get_credentials()
    
    if username in user_credentials and user_credentials[username] == password:
        print("Login válido!")
    else:
        print("Credenciais inválidas.")

    print("You have successfully logged in!")

def register_user():
    pass

#=====DynamoDB Connection===========
def connect_to_dynamodb():
     data = client.scan(TableName = "Tasks")
     return data

#=====Tasks CRUD===========

def view_all_tasks():
    with open('tasks_dynamodb_import.json', 'r') as file:
        for line in jsonfile:
                task = line.strip().split(", ")
                #This line is to split the line where there is a comma to make the task information more readable
                print(f"Assigned to: {task[0]}")
                print(f"Title: {task[1]}")
                print(f"Description: {task[2]}")
                print(f"Due Date: {task[3]}")
                print(f"Assigned Date: {task[4]}")
                print(f"Status: {task[5]}")
                print()
                  
def get_user_tasks():
    pass

def add_task():
    user_tasks["assigned_username"] = input("You can now assign tasks, please enter the username of the person you would like to assign tasks to: ")
    user_tasks["task_title"] = input("Please enter the title of the task: ")
    user_tasks["task_description"] = input("Please enter the task description: ")
    user_tasks["task_due_date"] = input("Please enter the due date of the task in the format dd/mm/yyyy:")
    user_tasks["assigned_date"] = input("Please enter the date today in the format dd/mm/yyyy:")


def view_my_tasks():
    pass
            
def store_to_dynamodb():
     pass

def main():
    while True:
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()
        if menu == 'r':
                new_username = input("To register a user, please enter the username of the new user: ").lower()
                new_password = input("Please enter the password for the new user: ").lower()
                confirmed_password = input("Please confirm the password for the new user: ").lower()
                while new_password != confirmed_password:
                        confirmed_password_retry = input("This does not match the previous password, please try again: ").lower()
                        if confirmed_password_retry == new_password:
                            # store_to_dynamodb()
                            print("New user successfully registered!")
                            break
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_tasks()
        elif menu == 'vm':
            view_my_tasks()
        elif menu == 'e':
            exit()
        else:
            print("You have entered an invalid input. Please try again")
            
            
main()
