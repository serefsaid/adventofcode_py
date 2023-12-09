import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(9,2023)

lines = puzzle_input.split('\n')

puzzle = [list(reversed(list(map(int,line.split())))) for line in lines]

def find_next_value(piece):
    all_arrays = [piece]
    done =False
    while not done:
        diff_array = []
        for num in range(1,len(piece)):
            diff = piece[num]-piece[num-1]
            diff_array.append(diff)
        all_arrays.append(diff_array)
        piece = diff_array
        #if len(list(set(diff_array)))==1:
        if len(list(set(diff_array)))==1 and diff_array[0]==0:
            done = True
    reversed_result = list(reversed(all_arrays))
    for array_index in range(1,len(reversed_result)):
        new_value = reversed_result[array_index-1][-1] + reversed_result[array_index][-1]
        reversed_result[array_index].append(new_value)
    return reversed_result[-1][-1]

total = 0
for piece in puzzle:
    total += find_next_value(piece)
print(total)