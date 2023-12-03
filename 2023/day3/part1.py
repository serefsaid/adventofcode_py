import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(3,2023)

lines = puzzle_input.split('\n')

import re

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
    number_matches = re.finditer(number_pattern, line)
    number_indexes = [(match.start(), match.end()) for match in number_matches]

    previous_symbol_indexes = [(match.start()-1, match.end()+1) for match in re.finditer(symbol_pattern, previous_line)]#increased range to include diagonal numbers
    next_symbol_indexes = [(match.start()-1, match.end()+1) for match in re.finditer(symbol_pattern, next_line)]#increased range to include diagonal numbers
    same_symbol_indexes = [(match.start()-1, match.end()+1) for match in re.finditer(symbol_pattern, line)]#increased range to include diagonal numbers
    numbers = []
    for index_pair in number_indexes:
        index_pair_included = False
        number = int(line[index_pair[0]:index_pair[1]])
        for previous_index_pair in previous_symbol_indexes:#are there adjacent symbol in previous line
            if ((index_pair[0]>=previous_index_pair[0] and index_pair[0]<previous_index_pair[1]) \
                or (index_pair[1]<=previous_index_pair[1] and index_pair[1]>previous_index_pair[0])) \
                and not index_pair_included:
                numbers.append(number)
                index_pair_included = True
                break
        if not index_pair_included:#if symbol at previos line caused this number to append do not continue
            for next_index_pair in next_symbol_indexes:#are there adjacent symbol in next line
                if ((index_pair[0]>=next_index_pair[0] and index_pair[0]<next_index_pair[1]) \
                    or (index_pair[1]<=next_index_pair[1] and index_pair[1]>next_index_pair[0])) \
                    and not index_pair_included:
                    numbers.append(number)
                    index_pair_included = True
                    break
            if not index_pair_included:
                for same_index_pair in same_symbol_indexes:#are there adjacent symbol in same line
                    if ((index_pair[0]>=same_index_pair[0] and index_pair[0]<same_index_pair[1]) \
                        or (index_pair[1]<=same_index_pair[1] and index_pair[1]>same_index_pair[0])) \
                        and not index_pair_included:
                        numbers.append(number)
                        break
                        # no index_pair_included notation needed. index_pair_included = True
    return sum(numbers)
    #return numbers

sum_puzzle = 0
for line_index in range(0,len(lines)):
    sum_puzzle+= find_line_sum(line_index)
print(sum_puzzle)