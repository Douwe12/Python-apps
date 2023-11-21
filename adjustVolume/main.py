import keyboard as kb
from functions import adjust_volume, get_system_volume

def shortcut(event):
    pressed_key = event.name
    print(pressed_key)
    current_volume = get_system_volume()
    if pressed_key == "ctrl + o":
        adjust_volume(0)
    elif pressed_key == "ctrl + m":
        adjust_volume(1)


kb.on_press(shortcut)

kb.wait("esc")
print("Exiting program")