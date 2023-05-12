from src import handler as lg

def alfred_main(request: str = ''):
    return lg.logic(request.lower().strip())

if __name__ == '__main__':
    try:
        alfred_main('')
    except KeyboardInterrupt:
        print('Interupted')

### LIST OF TASKS TO BE COMPLETED
# TODO: Allow Alfred to do speech to text recognition so I can speak to him rather than typing (Kinda like Iron man and Jarvis)
# TODO: Connect to DB and saved responses / questions for ML
# TODO: Allow Alfred to set reminders / write to Google Calendar...
