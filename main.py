from cupshelpers import Printer
from userEntry.login import *
from userEntry.signup import *
from chat import chat
from colorama import Fore, Style
import os

def clear_screen():
    # Verifica el sistema operativo y utiliza el comando adecuado para limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

def print_separator():
    print(Fore.YELLOW + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" )

def print_title():
    print_separator()
    texto = f"""{Fore.RESET}
    {Fore.RED}▒▐██▄▒▄██▌ ▐██ ██▄░▒█▌▐█▀▀█▌ {Fore.MAGENTA} Creado por David y Alvaro  
    {Fore.RED}░▒█░▒█░▒█   █▌ ▐█▒█▒█░▐█▄░▐▌                              
    {Fore.RED}▒▐█░░░░▒█▌ ▐██ ██░▒██▌▐██▄█▌                              
"""
    print(texto)
    print_separator()

def menu():
    clear_screen()
    print_title()



    while True:
        print("")
        print(Fore.BLUE + "1. Log in")
        print("2. Sign Up")
        print("")
        choice = input(f"{Fore.CYAN}Escoge: {Fore.BLACK}") 
        print("")
        print(Fore.LIGHTBLUE_EX + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃" )
        print("")

        if choice == "1":
            if login():  # Verifica si el inicio de sesión es exitoso
                return True  # Retorna True si el inicio de sesión es exitoso, para continuar con el chat
        elif choice == "2":
            signup()
        else:
            print(Fore.RED + "Elección no valida")
            print(Fore.RESET + Style.RESET_ALL)

menu()
