import random
import string
import logging

class Password():
    def __init__(self):
        self.logger = logging.getLogger(type(self).__qualname__)

    def create_password(self):
        new_password = ''
        try:
            pass_len = int(input('How many characters does the password need to be?: '))

            new_password = self.generate_password(pass_len)
        except Exception as e:
            self.logger.exception(e)

        return new_password

    def generate_password(self, pass_len: int = 16):
        result_str = ''
        try:
            words = string.ascii_letters + string.digits + string.punctuation
            result_str = ''.join(random.choice(words) for i in range(pass_len))

        except Exception as e:
            self.logger.exception(e)

        return result_str

