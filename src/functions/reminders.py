import chime
from threading import Timer
from functions.terminal_colors import colors as terminal_message

tc = terminal_message()

def set_reminder():
    reminder_message = input('What shall I remind you about?: ')
    reminder_time = float(input('In How many minutes?: ')) * 60

    Timer(reminder_time, alert, args=[reminder_message]).start()

def alert(reminder_message):
    chime.info()
    print(tc.reminder_message(reminder_message))

