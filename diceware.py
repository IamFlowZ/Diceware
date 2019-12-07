"""
    diceware main module
"""

import os
import sys
import argparse
import re
import random

my_parser = argparse.ArgumentParser(prog='diceware', description='Create a passphrase based on the diceware standard.', epilog='Stay safe!')
my_parser.add_argument('-n', '--num', type=int, help='Number of words to be concatanated.')
my_parser.add_argument('-r', '--replace', type=str, help='Comma delimited list of characters to replace in output. Formatted like, \"original:replacement\"(e.g. a:@,A:^)')

def retrieve_word_list():
    """ parse wordlist file into dictionary """
    split_list = {}
    with open(os.path.join(os.getcwd(), 'sources', 'diceware.wordlist.txt')) as list_file:
        word_list = list_file.readlines()
        for line in word_list:
            pattern = re.compile(r"[\d]{5}")
            result = pattern.match(line)
            if result is not None and len(str(result)) > 0:
                key_value = tuple(line.split('\t'))
                split_list[key_value[0]] = key_value[1].replace('\n', '')
    return split_list

def generate_keys(num_words):
    keys = []
    for _ in range(int(num_words)):
        key = ''
        for _ in range(5):
            key += (str(random.randint(1,6)))
        keys  = keys + [key]

    pwd = ''
    for key in keys:
        val = split_list[key]
        up = val[0].upper()
        temp = val[1:(len(val))]
        m_temp = up + temp
        pwd += m_temp

    return pwd

def get_num_words():
    print("With passwords, length > complexity.\nSo how many words would you like?\n")
    num_words = input()
    if num_words.isdecimal():
        return num_words
    else:
        print("Please enter how many words you would like in your password.")
        get_num_words()

def replace_char(input, old, new):
    return input.replace(old, new)

def make_changes(pswd):
    print("Please enter the character you wish to change, a \":\" followed by the new character.")
    changes = input()
    if len(changes) > 1 and ':' in changes:
        new_vals = changes.split(':')
        pswd = replace_char(pswd, new_vals[0], new_vals[1])
        return pswd
    else:
        make_changes(pswd)

def realtime_replace(pswd):
    print("Would you like to replace any of the other characters? (y/n)")
    answer = input()
    answer.strip()
    if answer.lower() == 'n' or answer.lower() == 'no':
        print("Thank you for using Diceware, goodbye =^)")
        return False
    elif answer.lower() == 'y' or answer.lower() == 'yes':
        pswd = make_changes(pswd)
        print(f'Your current password:\t\033[92m{pswd}\033[0m')
        realtime_replace(pswd)
    else:
        print("Please enter either y(yes) or n(no).")
        realtime_replace(pswd)

if __name__ == '__main__':
    args = my_parser.parse_args()
    split_list = retrieve_word_list()
    if args.num is not None:
        pswd = generate_keys(args.num)
    else:
        pswd = generate_keys(get_num_words())

    if args.replace is not None:
        replacements = args.replace.split(',')
        for replacement in replacements:
            new_vals = replacement.split(':')
            pswd = replace_char(pswd, new_vals[0], new_vals[1])
        print(f'Your current password:\t{pswd}')
        realtime_replace(pswd)
    else:
        realtime_replace(pswd)
