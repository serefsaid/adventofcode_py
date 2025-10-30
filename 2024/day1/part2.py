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
    even_number = evens[idx]
    odds_clone = odds.copy()
    similarity_score = 0
    while True:
        if even_number in odds_clone:
            odds_clone.remove(even_number)
            similarity_score += 1
        else:
            break
    total_distance += even_number * similarity_score


print(total_distance)
#python 2024/day1/part2.py