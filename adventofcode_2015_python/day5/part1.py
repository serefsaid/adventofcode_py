import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(5,2015)

lines = puzzle_input.split('\n')

def is_nice(string):
    vowel_rule = False
    vowel_count = 0
    last_char = ''
    repeat_rule = False
    nsfw_rule = False
    for char in string:
        if char in ['a','e','i','o','u']:
            vowel_count+=1
        if vowel_count==3:
            vowel_rule = True
        
        if last_char==char:
            repeat_rule = True

        if last_char+char in ['ab','cd','pq','xy']:
            nsfw_rule = True
        last_char = char[:]
    return vowel_rule and repeat_rule and not nsfw_rule

nice_count = 0

for line in lines:
    if is_nice(line):
        nice_count+=1
print(nice_count)