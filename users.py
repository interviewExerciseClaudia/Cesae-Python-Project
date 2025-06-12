# users.py
from data import database

def get_users():
    return database.keys()

def get_user(username):
    if username in get_users():
        return database[username]
    return False

def authenticate():
    username = input("Username: ").strip()
    if get_user(username):
        return username 
    else:
        return False

def register_user():
    username = input("Novo utilizador: ").strip()
    if not get_user(username):
        database[username] = { "tasks": [] }
        return username
    else:
        return False