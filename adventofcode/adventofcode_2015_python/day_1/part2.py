import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(1,2015)

floor = 0
move_counter = 0
basement_counter = 0
for instruction in puzzle_input:
    if instruction=='(':
        floor+=1
    elif instruction==')':
        floor-=1
    move_counter+=1
    if floor<0:
        basement_counter+=1
        print(move_counter)
        break