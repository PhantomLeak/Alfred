import calendar  # Converts daytime number into day of the week
from datetime import datetime  # Used to get current day of the week

from src import handler as lg


def alfred_main(i):
    return lg.logic(i.lower().strip())

if __name__ == '__main__':
    try:
        alfred_main(None)
    except KeyboardInterrupt:
        print('Interupted')

### LIST OF TASKS TO BE COMPLETED
# TODO: Allow Alfred to do speech to text recognition so I can speak to him rather than typing (Kinda like Iron man and Jarvis)
# TODO: Connect to DB and saved responses / questions for ML
# TODO: Create User classes to allow for individual profiles

##TODO:: Create a font-end for Alfred, maybe using flask or Javascript?
## TODO: Allow Alfred to set reminders / write to Google Calendar...
