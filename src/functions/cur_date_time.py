from datetime import datetime, timedelta

def get_date_time(response):
    if 'date' in response:
        return str(f"Today's date is {datetime.today().strftime('%Y-%m-%d')}")
    else:
        current_time = datetime.now().strftime('%I:%M %p')

        if current_time > '12:00:00':
            current_time = current_time - timedelta(hours=12)

        return str(f"The current time is {current_time}")