import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(5,2015)

lines = puzzle_input.split('\n')

def is_nice(string):
    pair_repeat_rule = False
    repeat_rule = False
    last_char = ''
    before_last_char = ''
    for char in string:
        pair = last_char + char
        if string.count(pair)>1 and len(pair)==2:
            pair_repeat_rule = True
        if before_last_char==char:
            repeat_rule = True
        before_last_char = last_char[:]
        last_char = char[:]
    return pair_repeat_rule and repeat_rule

nice_count = 0

for line in lines:
    if is_nice(line):
        nice_count+=1
print(nice_count)