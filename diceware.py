import os
import sys
import random

file_dir = os.getcwd()
file_name = '\diceware.wordlist.txt'
file_path = file_dir + file_name
word_list = open(file_path)

my_list = word_list.readlines()
split_list = {}

for item in my_list:
    temp = item.split()
    if len(temp) > 3 or len(temp) <=1:
        continue
    else:
        split_list.setdefault(temp[0], 0)
        split_list[temp[0]] = temp[1]

num_words = 0
key_len = 5
keys = []
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
            #print(split_list[item])

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

    #run = False    
    #run2 = False
    #sys.exit()



