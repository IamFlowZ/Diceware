"""
    diceware main module
"""

import os
import sys
import argparse
import re
import random

import password

my_parser = argparse.ArgumentParser(prog='diceware', description='''
    Create a passphrase based on the diceware standard.
    Use the "-i" flag to modify the password in real time.
    If you would rather have it output only once, run without the -i flag, and use the -n and/or -r flags instead.
    '''
)

my_parser.add_argument('-i', '--interactive', help='Interact with the password generation in realtime(OPTIONAL)', action='store_true')
my_parser.add_argument('-n', '--num', type=int, help='Number of words to be concatanated.')
my_parser.add_argument('-r', '--replace', type=str, help='Comma delimited list of characters to replace in output. Formatted like, \"original:replacement\"(e.g. a:@,A:^)')

def get_num_words():
    """ For use with interactive mode. Retrieves and validates input for target number of words. """
    print("With passwords, length > complexity.\nSo how many words would you like?\n")
    num_words = input()
    if num_words.isdecimal():
        return num_words
    else:
        print("Please enter how many words you would like in your password.")
        get_num_words()

def make_changes(pswd):
    """ For use with interactive mode. Retrieves and validates input for changing characters in the password. """
    print("Please enter the character you wish to change, a \":\" followed by the new character.")
    changes = input()
    if len(changes) > 1 and ':' in changes:
        new_vals = changes.split(':')
        pswd.replace_char(new_vals[0], new_vals[1])
        return pswd
    else:
        make_changes(pswd)

def realtime_replace(pswd):
    """ For use with interactive mode. Interactive mode event handler """
    print("Would you like to replace any of the other characters? (y/n)")
    answer = input()
    answer.strip()
    if answer.lower() == 'n' or answer.lower() == 'no':
        print("Thank you for using Diceware, goodbye =^)")
        return False
    elif answer.lower() == 'y' or answer.lower() == 'yes':
        pswd = make_changes(pswd)
        print(f'Your current password:\t\033[92m{pswd.password}\033[0m')
        realtime_replace(pswd)
    else:
        print("Please enter either y(yes) or n(no).")
        realtime_replace(pswd)

if __name__ == '__main__':
    args = my_parser.parse_args()
    pswd = password.Password()
    if args.num is not None:
        pswd.generate_pswd(args.num)
    elif args.interactive is True:
        pswd.generate_pswd(get_num_words())
    else:
        print('\33[31mERROR\033[0m: Please either pass a number to the \"-n\" flag or set \"-i\" and try again. See \"diceware -h\" for more details.')
        sys.exit(1)

    if args.replace is not None:
        replacements = args.replace.split(',')
        for replacement in replacements:
            new_vals = replacement.split(':')
            pswd.replace_char(new_vals[0], new_vals[1])

    print(f'Your current password:\t\033[92m{pswd.password}\033[0m')
    if args.interactive is True:
        realtime_replace(pswd)
