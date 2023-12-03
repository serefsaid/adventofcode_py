import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(2,2015)

lines = puzzle_input.split('\n')

total = 0
for line in lines:
    sizes = line.split('x')
    bower = int(sizes[0])*int(sizes[1])*int(sizes[2])
    total +=bower
    max_side = max(int(sizes[0]),int(sizes[1]),int(sizes[2]))#find max side to remove
    sizes.remove(str(max_side))
    wrapper = 2*(int(sizes[0])+int(sizes[1]))
    total +=wrapper

print(total)