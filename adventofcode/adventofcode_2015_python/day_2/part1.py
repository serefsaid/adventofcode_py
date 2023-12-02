import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(2,2015)

lines = puzzle_input.split('\n')

total_paper_feet = 0
for line in lines:
    sizes = line.split('x')
    paper_feet = (2*int(sizes[0])*int(sizes[1])) + (2*int(sizes[1])*int(sizes[2]))+ (2*int(sizes[0])*int(sizes[2]))
    min_side = min(int(sizes[0])*int(sizes[1]),int(sizes[1])*int(sizes[2]),int(sizes[0])*int(sizes[2]))
    paper_feet += min_side
    total_paper_feet+=paper_feet

print(total_paper_feet)