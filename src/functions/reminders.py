import chime
from threading import Timer
from functions.terminal_colors import colors as terminal_message
from datetime import datetime

tc = terminal_message()

def set_reminder(reminder):
    time_digit = None
    for i in reminder:
        if i.isdigit():
            time_digit = i
    
    before_keyword, keyword, after_keyword = reminder.partition(time_digit)
    
    reminder_time = set_reminder_time(float(time_digit), after_keyword)
    reminder_message = get_reminder_message(before_keyword, after_keyword)
    
    # Timer(reminder_time, alert, args=[reminder_message]).start()


# Set the specified time the user wishes to be reminded in 
def set_reminder_time(time, time_span):
    if 'minutes' in time_span or 'minute' in time_span:
        return (time * 60)
    elif 'hours' in time_span:
        return ((time * 60) * 60)
    elif 'days' in time_span or 'day' in time_span:
        return (time * 86400) # There are 86400 seconds in a day
    elif 'am' in time_span or 'pm' in time_span: # If the user specifies a time to set the reminder at
        if 'am' in time_span:
            time_def = 'AM'
        if 'pm' in time_span:
            time_def = 'PM'

        # Get / Set requested user time in hour:minute format
        requested_time = datetime.strptime(f'{int(time)} {time_def}', "%I %p")
        # requested_time_formatted = datetime.strftime(requested_time, "%H:%M")
        
        # Get / Set the current time in hour:minute format
        current_time = datetime.now()
        # current_time_formatted = datetime.strftime(current_time, "%H:%M")

        time_diff = (requested_time - current_time)
        print(time_diff)


# Get the message that is being reminded to the user
def get_reminder_message(before, after):
    keyword = ''
    return_message = ''

    if 'set a reminder to' in before or 'remind me to' in before:
        if 'set a reminder to' in before:
            keyword = 'set a reminder to'
        elif 'remind me to' in before:
            keyword = 'remind me to'

        before_keyword, keyword, after_keyword = before.partition(keyword)
        size = len(after_keyword)
        return_message = after_keyword[:size - 4]

    elif 'set a reminder to' in after or 'remind me to' in after:
        if 'set a reminder to' in after:
            keyword = 'set a reminder to'
        elif 'remind me to' in after:
            keyword = 'remind me to'

        before_keyword, keyword, after_keyword = after.partition(keyword)
        return_message = after_keyword
    
    return return_message


# Chime and display alert once the specified timespan has finished
def alert(reminder_message):
    chime.info()
    print(tc.reminder_message(reminder_message))