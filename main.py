import os

from users import *
from tasks import *

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    user_logged = None

    while True:
        clear_terminal()
        print("\n--- MENU PRINCIPAL ---")
        print("1. Registar utilizador")
        print("2. Login")
        print("3. Sair")
        op = input("Escolha uma opção: ")

        if op == '1': # Registrar
            username = register_user() 
            if username:
                print(f"Utilizador '{username}' registado com sucesso.")
            else:
                print("Utilizador já existe. Tente outro.")
        elif op == '2': # Logar
            user_logged = authenticate()
            if user_logged:
                print(f"Login efetuado como {username}")
                user_menu(user_logged)
            else:
                print("Utilizador não encontrado. Registe-se primeiro.")
        elif op == '3':
            print("Adeus!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input("Pressione ENTER para continuar...")

def user_menu(user_logged):
    while True:
        print(f"\n--- MENU {user_logged} ---")
        print("1. Adicionar tarefa")
        print("2. Editar tarefa")
        print("3. Remover tarefa")
        print("4. Listar tarefas pendentes")
        print("5. Marcar tarefa como concluída")
        print("6. Pesquisar tarefas")
        print("7. Ver estatísticas")
        print("8. Logout")
        opc = input("Escolha uma opção: ")

        if opc == '1':
            pass
            #adicionar_tarefa_ui(user)
        elif opc == '2':
            pass
            #edit_task(user)
        elif opc == '3':
            pass
            #delete_task(user)
        elif opc == '4':
            pass
            #list_tasks(user)
        elif opc == '5':
            pass
            #mark_as_complete(user)
        elif opc == '6':
            pass
            #search_task(user)
        elif opc == '7':
            pass
            #show_statistics(user)
        elif opc == '8':
            print(f"Logout de {user_logged}")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
