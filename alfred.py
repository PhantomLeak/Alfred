import alfred_logic as lg
from terminal_colors import colors as terminal_message
from datetime import datetime # Used to get current day of the week
import calendar # Converts daytime number into day of the week

tc = terminal_message()

def alfred_main(i) : 

    if i is None:
        today = calendar.day_name[datetime.today().weekday()]

        user_input = input(tc.prompt_message(f'Hello Sir, how can I help you on this fine {today}?:')).lower()

        lg.logic(user_input)
    else:
        today = calendar.day_name[datetime.today().weekday()]
        user_input = input(tc.prompt_message('Is there anything else I can help you with?:')).lower()
        lg.logic(user_input)

# Allows other files to call method without looping error
if __name__ == '__main__':
    try:
        alfred_main(None)
    except KeyboardInterrupt: #Check for keyboard Interruptions...error seems to constantly show up when searching the web.
        print(tc.error_message('Interrupted'))


#TODO Allow Alfred to do speech to text recognition so I can speak to him rather than typing (Kinda like Iron man and Jarvis)
# May be an issue, pyaudio doesn't seem to want to work on windows machines, may need to install this on raspberryPi

###Todo: Create more games...maybe something like the snake game or hangman? come back to this...
###Todo: Update search to auto search if input in question (Updated search for a more streamline approach but still need to nail down the process)
###Todo: Look into phone connections and allowing alfred to send texts, emails, and make calls.