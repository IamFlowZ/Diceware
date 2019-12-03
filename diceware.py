"""
    diceware main module
"""
import os
import re
import sys
import random

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

if __name__ == '__main__':
    num_words = 0
    key_len = 5
    keys = []
    split_list = retrieve_word_list()
    print("With passwords, length > complexity.\nSo how many words would you like?\n")

    run = True
    while(run):
        num_words = input()
        if num_words.isdecimal():
            for i in range(int(num_words)):
                key = ''
                for j in range(key_len):
                    key += (str(random.randint(1,6)))

                keys  = keys + [key]

            pwd = ''
            for item in keys:
                val = split_list[item]
                up = val[0].upper()
                temp = val[1:(len(val))]
                m_temp = up + temp
                pwd += m_temp

            print(pwd)
            run = False
        else:
            print("Please enter how many words you would like in your password.")

    run2 = True
    while run2:
        print("Would you like to replace any letters with special characters? (y/n)")
        answer = input()
        answer.strip()
        
        if answer.lower() == 'n':
            print("Thank you for using Diceware, goodbye =^)")
            run2 = False
            sys.exit()
            
        elif answer.lower() == 'y':
            print("Please enter how many characters you would like to replace,")
            num_changes = input()
            if num_changes.isdecimal():
                for n in range(int(num_changes)):
                    print("Please enter the character you wish to change, followed by new character.")
                    changes = input()
                    if len(changes) > 1:
                        changes.split(" ")
                        temp = list(pwd)
                        for i in range(len(pwd)):
                            if temp[i] == changes[0]:
                                temp[i] = changes[2]
                        pwd = "".join(temp)
                        print("Here's your new password, " + pwd)
                    else:
                        print("Please enter the character you wish to replace followed by the new character")
                
            else:
                print("Please enter the number of characters you would like to replace")
                    
        elif answer.lower() != 'y' or 'n':
            print("Please enter either yes or no.")
