# tasks.py
import users
from data import database 
from datetime import datetime
import main
import sys
import os

priorities_dict = {
    "HIGHEST" : 1,
    "HIGH" : 2,
    "MEDIUm" : 3,
    "LOW" : 4,
    "LOWEST" : 5 
}

categories_dict = {
    "Maintenance" : 1, 
    "New Feature" : 2 , 
    "Research" : 3 , 
    "Documentation" : 4
}

continue_flag = ""

def get_tasks_by_user(username):
    main.clear_terminal()
    for k,v in database:
        if k == username:
            tasks = database[username]["tasks"]
        else :
            print("Unidentified user!")
    return tasks

def get_my_tasks():
    main.clear_terminal()
    username = users.get_user()
    try :
        for k,v in database:
            if k == username:
                tasks = database[username]
    except :
        print("You don't seem to have assigned tasks yet!")
    return tasks

def get_all_tasks():
    return database.values()

def add_new_task():
    main.clear_terminal()
    while(True):
        # EU TENHO A CERTEZA COMO IR BUSCAR O USER
        username = users.get_user()
        
        title = input("Please insert a title for the task to be introduced : ").lower()
        
        description = input("Please insert a short description for the task to be introduced : ").lower()
        
        print(f"\n--- TASK PRIORITIES  ---")
        print("1. Highest")
        print("2. High")
        print("3. Medium")
        print("4. Low")
        print("5. Lowest")
        
        priority = int(input("From the list above, please asign a priority to your task : "))
        
        for k,v in priorities_dict:
            if v not in priorities_dict:
                priority = int(input("Please insert a valid priority : "))
                break
            
        due_date = datetime(input("Please insert the due date (YYYY, MM, DD) for the task to be introduced : ")).strftime("%Y/%m/%d")       
        assigned_date = datetime.now()
        
        print(f"\n--- TASK CATEGORIES  ---")
        print("1. Maintenance")
        print("2. New Feature")
        print("3. Research")
        print("4. Documentation")
        
        category = int(input("Please designate a valid category for the task you wish to insert: "))
        
        for k,v in categories_dict:
            if v not in priorities_dict:
                category = int(input("Please insert a valid category : "))
                break
        try :
        # JA NAO E RECORDO SE OS DICIONARIOS SAO MUTAVEIS OU IMUTAVEIS E SE ISTO VAI SUBSTITUIR ALGUA TAREFA QUE AQUELE UTILIZADOR JA TENHA NA LISTA DE TASKS
            database[username] = { "tasks": [{
                    "title": title,
                    "description" : description,
                    "priority": priority,
                    "due_date": due_date,
                    "assigned_date": assigned_date,
                    "category": category
            }] }
        except :
            continue_flag = input("The task hasn't been  inserted! Do you wish to insert another task ? (y,n) ").lower()
    
        if continue_flag == "n":
            break
        
def remove_task(username, title):
        main.clear_terminal()
        try :
            username = users.get_user()
            try :
                tasks = get_my_tasks()
                for task in tasks:
                    for k,v in task:
                        if v == title:
                            database[username].pop(task)            
            except :
                print("This user does not see to have any task assigned yet!")
                # sys.exit()
        except :
            print("Unidentified user")
            # sys.exit()
       
def edit_task(username, title):
        main.clear_terminal()
        try :
            username = users.get_user()
            try :
                tasks = get_my_tasks()
                for task in tasks:
                    for k,v in task:
                        if v == title:
                            remove_task(username, title)
                            add_new_task()
            except :
                print("This user does not see to have any task assigned yet!")
                # sys.exit()
        except :
            print("Unidentified user")
            # sys.exit()
            
    

