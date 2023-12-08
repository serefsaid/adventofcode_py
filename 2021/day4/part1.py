import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(4,2021)

lines = puzzle_input.split('\n\n')
directions,*hands = lines
directions = [int(direction) for direction in directions.split(',')]
hands = [[[int(value) for value in line.split()]for line in hand] for hand in [hand.split('\n') for hand in hands]]