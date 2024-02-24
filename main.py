import pyautogui
from time import sleep
import pynput
from pynput.keyboard import Listener

running = False

def on_press(key):
    global running
    if key == pynput.keyboard.KeyCode.from_char('k'):
        running = not running
        if running:
            print('Macro has started')
        else:
            print('Macro has stopped')


listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()

while True:
    if running:
        pyautogui.click(1341, 372)
        pyautogui.click(1261, 372)
        sleep(0.1)
