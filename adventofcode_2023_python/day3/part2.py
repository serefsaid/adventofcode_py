import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(3,2023)

lines = puzzle_input.split('\n')

import re
from functools import reduce

def find_line_sum(index):
    line = lines[index]
    if index>0:#if given line is first one there is no previous line
        previous_line = lines[index-1]
    else:
        previous_line = ''
    if index<len(lines)-1:#if given line is last one there is no next line
        next_line = lines[index+1]
    else:
        next_line = ''

    symbol_pattern = f"[^.0123456789]+"#exclude dots and figures to find symbols
    number_pattern = f"[0123456789]+"
    symbol_matches = re.finditer(symbol_pattern, line)
    symbol_indexes = [(match.start(), match.end()) for match in symbol_matches]

    previous_number_indexes = [(match.start()-1, match.end()+1) for match in re.finditer(number_pattern, previous_line)]#increased range to include diagonal numbers
    next_number_indexes = [(match.start()-1, match.end()+1) for match in re.finditer(number_pattern, next_line)]#increased range to include diagonal numbers
    same_number_indexes = [(match.start()-1, match.end()+1) for match in re.finditer(number_pattern, line)]#increased range to include diagonal numbers
    numbers = []
    for index_pair in symbol_indexes:
        gears = []
        gear_counter = 0
        for previous_index_pair in previous_number_indexes:#are there adjacent number in previous line
            gear = int(previous_line[previous_index_pair[0]+1:previous_index_pair[1]-1])
            if ((index_pair[0]>=previous_index_pair[0] and index_pair[0]<previous_index_pair[1]) \
                or (index_pair[1]<=previous_index_pair[1] and index_pair[1]>previous_index_pair[0])):
                gears.append(gear)
                gear_counter+=1
        for next_index_pair in next_number_indexes:#are there adjacent number in next line
            gear = int(next_line[next_index_pair[0]+1:next_index_pair[1]-1])
            if ((index_pair[0]>=next_index_pair[0] and index_pair[0]<next_index_pair[1]) \
                or (index_pair[1]<=next_index_pair[1] and index_pair[1]>next_index_pair[0])):
                gears.append(gear)
                gear_counter+=1
        for same_index_pair in same_number_indexes:#are there adjacent number in same line
            gear = int(line[same_index_pair[0]+1:same_index_pair[1]-1])
            if ((index_pair[0]>=same_index_pair[0] and index_pair[0]<same_index_pair[1]) \
                or (index_pair[1]<=same_index_pair[1] and index_pair[1]>same_index_pair[0])):
                gears.append(gear)
                gear_counter+=1
        if gear_counter==2:#check if 2 adjacent part number
            numbers.append(reduce(lambda x,y : x*y,gears))#multiplying for gear ratio
    result = 0
    if len(numbers)>0:#check if numbers list is blank
        result+=sum(numbers)
    return result

sum_puzzle = 0
for line_index in range(0,len(lines)):
    sum_puzzle+= find_line_sum(line_index)
print(sum_puzzle)