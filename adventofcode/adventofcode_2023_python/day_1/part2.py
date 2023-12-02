import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(1,2023)
lines = puzzle_input.split('\n')


import re

numbers = [
    ['zero','0']
    ,['one','1']
    ,['two','2']
    ,['three','3']
    ,['four','4']
    ,['five','5']
    ,['six','6']
    ,['seven','7']
    ,['eight','8']
    ,['nine','9']
]

all_numbers = [
    'zero','0'
    ,'one','1'
    ,'two','2'
    ,'three','3'
    ,'four','4'
    ,'five','5'
    ,'six','6'
    ,'seven','7'
    ,'eight','8'
    ,'nine','9'
]
        

def replace_words_with_int(line):
    newStr = line[:]
    first_found = False
    last_found = False
    for number in numbers:
        if number[0] in line:
            indexes = find_all_indexes(line,number[0])
            #index = line.find(number[0])
            number_char_len = len(number[0])
            for index in indexes:
                first_error_counter = False#check if there is an number before that
                last_error_counter = False
                for all_number in all_numbers:
                    if all_number in line[:index+number_char_len-1] and not first_found:
                        first_error_counter=True
                    if all_number in line[index+1:] and not last_found:
                        last_error_counter=True
                if not first_error_counter and not first_found:
                    newStr = newStr.replace(number[0],number[1],1)
                    first_found = True
                if not last_error_counter and not last_found:
                    newStr = number[1].join(newStr.rsplit(number[0],1))
                    last_found = True
    return newStr

def find_all_indexes(text, substring):
    return [m.start() for m in re.finditer(substring, text)]

def find_first_and_last_int(str):
    str = replace_words_with_int(str)
    ints = ''.join(c for c in str if c.isdigit())
    result = ints[0] + '' + ints[len(ints)-1]
    return int(result)

sum = 0
for line in lines:
    new_int = find_first_and_last_int(line)
    sum += new_int

print(sum)