import logging
import random
import string
import re


class Password():
    def __init__(self):
        self.logger = logging.getLogger(type(self).__qualname__)

    def create_password(self, password_obj):
        new_password = ''

        pass_len = password_obj.get('passlen')
        selected_password_type = password_obj.get('selectedPasswordType')
        use_special_characters = password_obj.get('useSpecialCharacters')

        if not pass_len or not selected_password_type or use_special_characters is None:
            return 'To Generate a password, all fields must be completed'

        try:
            new_password = self.generate_password(pass_len=pass_len, selected_password_type=selected_password_type, use_special_characters=use_special_characters)
        except Exception as e:
            self.logger.exception(e)

        return new_password

    def generate_password(self, pass_len, selected_password_type, use_special_characters):
        result_str = ''
        try:
            words = string.ascii_letters

            if selected_password_type == 'alphanumeric':
                words += string.digits

            if use_special_characters:
                words += string.punctuation

            result_str = ''.join(random.choice(words) for i in range(pass_len))

        except Exception as e:
            self.logger.exception(e)

        return result_str

