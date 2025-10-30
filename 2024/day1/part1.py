import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(1,2024)

lines = puzzle_input.split('\n')

evens = []
odds = []
for line in lines:
    splitted_line = line.split("   ")
    evens.append(int(splitted_line[0]))
    odds.append(int(splitted_line[1]))

total_distance = 0
for idx in range(0,len(lines)):
    min_even = min(evens)
    min_odd = min(odds)
    total_distance += abs(min_even-min_odd)
    evens.remove(min_even)
    odds.remove(min_odd)


print(total_distance)
#python 2024/day1/part1.py