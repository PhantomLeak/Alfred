import logging
import random
import string
import re


class Password():
    def __init__(self):
        self.logger = logging.getLogger(type(self).__qualname__)

    def create_password(self, password_init):
        new_password = ''
        pass_len = 16

        try:
            if any(char.isdigit() for char in password_init):
                pass_len = re.findall(r'\d+', password_init)[0]
            
            new_password = self.generate_password(pass_len=int(pass_len))
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

