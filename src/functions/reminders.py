import logging
import re
from threading import Timer
from tkinter import messagebox

import chime


def set_reminder(reminder):
    try:
        # Use positive lookbehind to get the next word after 'in'
        time_digit = re.search('(?<=in )(\w+)', reminder).group(1)  # Get the first parenthesised subgroup from regex search

        before_keyword, keyword, after_keyword = reminder.partition(time_digit)

        reminder_time = set_reminder_time(float(time_digit), after_keyword)

        reminder_message = get_reminder_message(before_keyword, after_keyword)

        Timer(reminder_time, alert, args=[reminder_message]).start()
    except Exception as e:
        logging.exception(e)


# Set the specified time the user wishes to be reminded in 
def set_reminder_time(time: float, time_span: str):
    if 'seconds' in time_span:
        return time
    if 'minutes' in time_span or 'minute' in time_span:
        return time * 60
    elif 'hours' in time_span:
        return (time * 60) * 60
    elif 'days' in time_span or 'day' in time_span:
        return time * 86400  # There are 86400 seconds in a day
    # elif 'am' in time_span or 'pm' in time_span:  # If the user specifies a time to set the reminder at
    #     time_def = 'AM'
    #     if 'am' in time_span:
    #         requested_time = datetime.strptime(f'{int(time)} AM', "%I %p")
    #     else:
    #         requested_time = datetime.strptime(f'{int(time)} PM', "%I %p")
    #
    #     # Get / Set the current time in hour:minute format
    #     current_time = datetime.now()
    #     # current_time_formatted = datetime.strftime(current_time, "%H:%M")
    #
    #     time_diff = (requested_time - current_time)
    #     print(time_diff)


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
    return reminder_message
    # try:
    #     chime.info()
    #     messagebox.showinfo("Reminder", reminder_message)
    # except Exception as e:
    #     logging.exception(e)
