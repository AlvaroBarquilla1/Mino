import subprocess

def install_requirements():
    try:
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("Paquetes instalados exitosamente.")
    except subprocess.CalledProcessError as e:
        print("Error al instalar los paquetes:", e)

if __name__ == "__main__":
    install_requirements()
