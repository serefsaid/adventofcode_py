import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(6,2023)

lines = puzzle_input.split('\n')

total_time = int(lines[0].split(':')[1].replace(' ',''))
total_distance = int(lines[1].split(':')[1].replace(' ',''))

def find_possibilities(total_time,total_distance):
    possibility = 0
    for time in range(1,total_time):#time stands for button press time
        left_time = total_time-time
        distance = left_time*time
        if distance>total_distance:
            possibility+=1
    return possibility

print(find_possibilities(total_time,total_distance))