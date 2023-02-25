import calendar  # Converts daytime number into day of the week
from datetime import datetime  # Used to get current day of the week

import handler as lg
from functions.terminal_colors import colors as terminal_message

tc = terminal_message()


def alfred_main(i):
    return lg.logic(i.lower().strip())
    # if i is None:
    #     today = calendar.day_name[datetime.today().weekday()]

    #     user_input = input(tc.prompt_message(f'Hello Sir, how can I help you on this fine {today}?:')).lower()
    #     lg.logic(user_input.strip())

    # else:
    #     user_input = input(tc.prompt_message('Is there anything else I can help you with?:')).lower()
    #     lg.logic(user_input.strip())


if __name__ == '__main__':
    try:
        alfred_main(None)
    except KeyboardInterrupt:
        print(tc.error_message('Interrupted'))

### LIST OF TASKS TO BE COMPLETED
# TODO: Allow Alfred to do speech to text recognition so I can speak to him rather than typing (Kinda like Iron man and Jarvis)
# TODO: Connect to DB and saved responses / questions for ML
# TODO: Create User classes to allow for individual profiles

##TODO:: Create a font-end for Alfred, maybe using flask or Javascript?
## TODO: Allow Alfred to set reminders / write to Google Calendar...
