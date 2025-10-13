import pyautogui
import time
import threading
import keyboard

while (not keyboard.is_pressed("å")):
    True

direction = 4

def listen_for(key, action):
    while True:
        if keyboard.is_pressed(key):
            action()
        time.sleep(0.1)
def action_1():
    global direction
    direction = 0
def action_3():
    global direction
    direction = 1
def action_e():
    global direction
    direction = 2
def action_q():
    global direction
    direction = 3
def action_g():
    global direction
    direction = 4

threading.Thread(target=listen_for, args=("1", action_1), daemon=True).start()
threading.Thread(target=listen_for, args=("3", action_3), daemon=True).start()
threading.Thread(target=listen_for, args=("e", action_e), daemon=True).start()
threading.Thread(target=listen_for, args=("q", action_q), daemon=True).start()
threading.Thread(target=listen_for, args=("g", action_g), daemon=True).start()

while True:
    if (direction == 0):
        pyautogui.press("a")
        pyautogui.press("w")
    if (direction == 1):
        pyautogui.press("w")
        pyautogui.press("d")
    if (direction == 2):
        pyautogui.press("d")
        pyautogui.press("s")
    if (direction == 3):
        pyautogui.press("s")
        pyautogui.press("a")