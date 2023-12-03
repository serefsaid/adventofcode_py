import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(1,2023)

lines = puzzle_input.split('\n')

def find_first_and_last_int(str):
    ints = ''.join(c for c in str if c.isdigit())
    result = ints[0] + '' + ints[len(ints)-1]
    return int(result)

sum = 0
for line in lines:
    sum += find_first_and_last_int(line)

print(sum)