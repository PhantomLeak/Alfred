import calendar  # Converts daytime number into day of the week
from datetime import datetime  # Used to get current day of the week


def greeting():
    today = calendar.day_name[datetime.today().weekday()]
    return f"Hello Sir, I'm Alfred, how can I help you on this fine {today}?"
