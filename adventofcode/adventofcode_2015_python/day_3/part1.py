import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(3,2015)


def find_gifted_houses_count(puzzle):
    x = 0
    y = 0
    delivered_directions = [[x,y]]
    for direction in puzzle:
        if direction=='^':
            y+=1
        elif direction=='v':
            y-=1
        elif direction=='<':
            x-=1
        elif direction=='>':
            x+=1
        
        if [x,y] not in delivered_directions:
            delivered_directions.append([x,y])
    return len(delivered_directions)

print(find_gifted_houses_count(puzzle_input))