from queue import Empty
import pytssx3 as speak
import alfred_logic as lg
from datetime import datetime # Used to get current day of the week
import calendar # Converts daytime number into day of the week

def alfred_main(i) : 
    if i is None:
        today = calendar.day_name[datetime.today().weekday()]
        user_input = input(f'Hello sir, how can I help you on this fine {today}? : ')
        lg.logic(user_input)
    else:
        today = calendar.day_name[datetime.today().weekday()]
        user_input = input('Is there anything else I can help you with? : ')
        lg.logic(user_input)

# Allows other files to call method without looping error
if __name__ == '__main__':
    alfred_main(None)


#TODO Allow Alfred to do speech to text recognition so I can speak to him rather than typing (Kinda like Iron man and Jarvis)
# May be an issue, pyaudio doesn't seem to want to work on windows machines, may need to install this on raspberryPi
#TODO use an API for practice, maybe a weather API to get local weather forcasts? 