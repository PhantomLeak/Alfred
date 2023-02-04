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
        pass

    # Custom message with color options rather than a set color output
    def terminal_message(self, color: str, message: str):
        message = f'{self.pref}{color}{message}{self.reset} '

        return message

    # Standard used prompt message when prompting for input
    def prompt_message(self, message: str):
        message = f'{self.pref}{self.green}{message}{self.reset} '

        return message

    def prompt_message_choices(self, number: int, option: str):
        message = f'{self.pref}{self.yellow}{number}{self.reset}{self.pref}{self.green}{option}{self.reset} '

        return message

    # Standard output message returned to user 
    def output_message(self, message: str):
        message = f'\n{self.pref}{self.cyan}{message}{self.reset}\n'

        return message

    def output_with_return_message(self, message: str, output: str):
        message = f'{message} {self.pref}{self.cyan}{output}{self.reset}'

        return message

    # Standard error message when error is caught
    def error_message(self, message: str):
        message = f'{self.pref}{self.red}{message}{self.reset} '

        return message

    def reminder_message(self, message: str):
        message = f'\n---------------\n{self.pref}{self.yellow}Reminder: {message}{self.reset}\n---------------\n'

        return message
