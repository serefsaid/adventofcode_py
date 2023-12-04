import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(4,2023)

lines = puzzle_input.split('\n')


def parse(line):
    game_part = line.split(':')[1]
    seperated = game_part.split('|')
    winning_numbers = list(filter(None, seperated[0].split(' ')))
    my_numbers = list(filter(None, seperated[1].split(' ')))
    result = {
        "winning_numbers":winning_numbers
        ,"my_numbers":my_numbers
    }
    return result

def calculate_point(line):
    data = parse(line)
    point = 0
    power = 0
    for winning_number in data['winning_numbers']:
        if winning_number in data['my_numbers']:
            point = 2 ** power
            power +=1
    return point

sumbit = 0
for line in lines:
    sumbit += calculate_point(line)
print(sumbit)