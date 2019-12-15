"""
    Password module
"""

import os
import re
import random

class Password():
    """
        Create and modifiy a password

        Methods
        -------
        retrieve_word_list
            parse wordlist file into dictionary
        generate_pswd(num_words: int)
            generates a new password
        replace_char(old: str, new: str)
            replace an old character with a new character

        Attributes
        ----------
        word_list: list
            contains the parsed wordlist file
        password: str
            current password iteration
    """
    def retrieve_word_list(self):
        """ parse wordlist file into dictionary """
        split_list = {}
        try:
            with open(os.path.join(os.getcwd(), 'sources', 'diceware.wordlist.asc')) as list_file:
                for line in list_file.readlines():
                    pattern = re.compile(r"[\d]{5}")
                    result = pattern.match(line)
                    if result is not None and len(str(result)) > 0:
                        key_value = tuple(line.split('\t'))
                        split_list[key_value[0]] = key_value[1].replace('\n', '')
            self.word_list = split_list
        except FileNotFoundError:
            raise(FileNotFoundError('Please install the dicelist sources.'))

    def generate_pswd(self, num_words):
        """ generates a new password """
        keys = []
        for _ in range(int(num_words)):
            key = ''
            for _ in range(5):
                key += (str(random.randint(1,6)))
            keys  = keys + [key]

        pwd = ''
        for key in keys:
            val = self.word_list[key]
            upper_first_val = val[0].upper() + val[1:(len(val))] # Uppercasing the first letter in the value.
            pwd += upper_first_val

        self.password = pwd

    def replace_char(self, old, new):
        self.password = self.password.replace(old, new)

    def __init__(self):
        self.retrieve_word_list()