import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(5,2024)
parts = puzzle_input.split('\n\n')
rules = parts[0].split('\n')
updates = parts[1].split('\n')
print(rules,1)
#print(updates,2)
total_middle_page = 0

print(total_middle_page)
#python 2024/day5/part1.py