import bcrypt
import os
import datetime
from colorama import Fore, Style
from speech_recognized import *  

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def login():
    print(Fore.GREEN + "Has seleccionado la opción de "+ Fore.WHITE + "Login")
    print("")
    username = input(f"{Fore.GREEN}Ingresa el usuario: ")
    password = input("Ingresa la contraseña: ")

    filepath = os.path.join("usuarios", "credentials.txt")
    with open(filepath, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 3:
                _, user, hashed_password = parts  
                if user == username:
                    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                        log_entry(username, "login")
                        audioTexto()

                        return True


                    else:
                        print("Contraseña incorrecta")
                        return False

    print("")                
    print(Fore.LIGHTBLUE_EX + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃" )
    print("")                

    print("Usuario no encontrado")
    return False

def log_entry(username, action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filepath = os.path.join("registro_de_actividad", "log.txt")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "a") as file:
        file.write(f"{timestamp}: {username} {action}\n")

