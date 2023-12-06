import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(6,2023)

lines = puzzle_input.split('\n')

times = [int(x) for x in lines[0].split(':')[1].split()]
distances = [int(x) for x in lines[1].split(':')[1].split()]

data = tuple(zip(times,distances))

def find_possibilities(puzzle):
    possibilities = 1#to multiply all races
    for piece in puzzle:
        possibility = 0#just for this race
        total_time = piece[0]
        total_distance = piece[1]
        for time in range(1,total_time):#time stands for button press time
            left_time = total_time-time
            distance = left_time*time
            if distance>total_distance:
                possibility+=1
        possibilities *= possibility
    return possibilities

print(find_possibilities(data))