from email.mime import audio
from chat import *
import os
from colorama import Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def audioTexto():
    import speech_recognition as sr

    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            clear_screen()

            print("Esperando a 'Oye Mino'...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='es-ES')
            if "oye" in text.lower():  # Verifica si se mencionó "Oye Mino"
                reconocimientoVoz()  # Comienza el reconocimiento de voz normal
                break
        except sr.UnknownValueError:
            print("Mino no ha podido entender el audio")
        except sr.RequestError as e:
            print("No hay acceso al servicio de reconocimiento de voz de Google; {0}".format(e))

def reconocimientoVoz():
    import speech_recognition as sr

    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Di algo...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language='es-ES')
            if "close" in text.lower():
                print("Mino ha entendido: " + text)
                print("Deteniendo la escucha...")
                break
            else:
                print("Mino ha entendido: " + text)
                chat(text)  # Pasa el texto reconocido al chat
        except sr.UnknownValueError:
            print("Mino no ha podido entender el audio")
        except sr.RequestError as e:
            print("No hay acceso al servicio de reconocimiento de voz de Google; {0}".format(e))
