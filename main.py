import keyboard
from datetime import datetime


def write_date_time(file_name):
    current_date_time = datetime.now().strftime("Date: %A, %m/%d/%Y   Time: %I:%M:%S %p")
    with open(file_name, 'a') as file:
        file.write(current_date_time + '\n')


def on_tab_press(e):
    if e.event_type == keyboard.KEY_DOWN and e.name == 'tab':
        write_date_time(r"\your\folder\path\here")
        write_date_time(r"\your\folder\path\here")


keyboard.hook(on_tab_press)

try:
    keyboard.wait('esc')  # Wait for the 'esc' key to exit the program
except KeyboardInterrupt:
    pass
finally:
    keyboard.unhook_all()
