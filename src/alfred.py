import alfred_logic as lg
from functions.terminal_colors import colors as terminal_message
from datetime import datetime # Used to get current day of the week
import calendar # Converts daytime number into day of the week

tc = terminal_message()

def alfred_main(i) : 
    if i is None:
        today = calendar.day_name[datetime.today().weekday()]

        user_input = input(tc.prompt_message(f'Hello Sir, how can I help you on this fine {today}?:')).lower()

        lg.logic(user_input)
    else:
        user_input = input(tc.prompt_message('Is there anything else I can help you with?:')).lower()
        lg.logic(user_input)

if __name__ == '__main__':
    try:
        alfred_main(None)
    except KeyboardInterrupt:
        print(tc.error_message('Interrupted'))


#TODO Allow Alfred to do speech to text recognition so I can speak to him rather than typing (Kinda like Iron man and Jarvis)

#TODO Allow Alfred to set reminders / write to Google Calendar...

##TODO: Update search to auto search if input in question (Updated search for a more streamline approach but still need to nail down the process)
##TODO: Fix logic to handle a standard conversation (How are you?) and hold a conversation...
##TODO: Create a font-end for Alfred, maybe using flask or Javascript? 

###TODO: Create more games...maybe something like the snake game or hangman? come back to this...
###TODO: Look into phone connections and allowing alfred to send texts, emails, and make calls.
###TODO: Clean up weather inputs...Response works but the temperature comes back with odd numbers