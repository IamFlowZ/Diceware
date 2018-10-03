import os
import random

file_dir = 'C:\\Users\\Admin\\Desktop\\Diceware\\'
file_name = 'diceware.wordlist.txt'
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

num_words = input()

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
