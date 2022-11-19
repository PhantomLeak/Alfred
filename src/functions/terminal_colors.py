import logging

# ANSI coloring for terminal output messages
class colors:
    pref = "\033["
    reset = f"{pref}0m"
    black = "30m"
    red = "31m"
    green = "32m"
    yellow = "33m"
    blue = "34m"
    magenta = "35m"
    cyan = "36m"
    white = "37m"


    def __init__(self):
        self.logger = logging.getLogger(type(self).__qualname__)

    # Custom message with color options rather than a set color output
    def terminal_message(self, color, message):
        try:
            message = f'{self.pref}{color}{message}{self.reset} '
        except Exception as e:
            self.logger(e)

        return message
    
    # Standard used prompt message when promting for input
    def prompt_message(self, message):
        try: 
            message = f'{self.pref}{self.green}{message}{self.reset} '
        except Exception as e:
            self.logger(e)

        return message

    def prompt_message_choices(self, number, option):
        try: 
            message = f'{self.pref}{self.yellow}{number}{self.reset}{self.pref}{self.green}{option}{self.reset} '
        except Exception as e:
            self.logger(e)

        return message
    
    # Standard output message returned to user 
    def output_message(self, message):
        try: 
            message = f'\n{self.pref}{self.cyan}{message}{self.reset}\n'
        except Exception as e:
            self.logger(e)

        return message

    # Standard error message when error is caught
    def error_message(self, message):
        try: 
            message = f'{self.pref}{self.red}{message}{self.reset} '
        except Exception as e:
            self.logger(e)

        return message

    def reminder_message(self, message):
        try:
            message = f'\n---------------\n{self.pref}{self.yellow}Reminder: {message}{self.reset}\n---------------\n'
        except Exception as e:
            self.logger(e)
        
        return message
    