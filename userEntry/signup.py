import bcrypt
import os
import datetime
import os
import sys
from colorama import Fore, Style

sys.stderr = open(os.devnull, 'w')
def encrypt_password(password):
    # Hash de la contraseña utilizando bcrypt
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def save_credentials(username, hashed_password):
    filepath = os.path.join("usuarios", "credentials.txt")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "a") as file:
        timestamp = data().strftime("%Y-%m-%d %H-%M-%S")[:19]
        file.write(f"{timestamp}:{username}:{hashed_password.decode('utf-8')}\n")

def data():
    return datetime.datetime.now()

def signup():
    print(Fore.GREEN + "Has seleccionado la opación de " + Fore.WHITE + "registro")
    username = input(f"{Fore.GREEN}Ingresa el usuario: ")

    # Verificar si el usuario ya existe
    if verify_credential(username):
        print("ERES BOBO? YA ESTA REGISTRADO")
        return
    
    password = input("Ingresa la contraseña: ")
    hashed_password = encrypt_password(password)
    save_credentials(username, hashed_password)
    print("Ole campeon que has entrado")

def verify_credential(username):
    filepath = os.path.join("usuarios", "credentials.txt")
    if not os.path.isfile(filepath):
        return False
    with open(filepath, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 3:
                timestamp, saved_username, hashed_password = parts
                if username == saved_username:
                    return True
    return False

def menu():
    while True:
        print("1. Log in")
        print("2. Sign Up")
        choice = input("Escoge: ")
        if choice == "1":
            # Implementar la funcionalidad de inicio de sesión
            pass
        elif choice == "2":
            signup()
        else:
            print("Elección no valida")

if __name__ == "__main__":
    menu()
