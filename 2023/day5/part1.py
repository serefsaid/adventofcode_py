import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(5,2023)

parts = puzzle_input.split('\n\n')

seed , *maps = parts
print(*maps)