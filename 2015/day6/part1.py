import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(6,2015)

lines = puzzle_input.split('\n')

def parse_instruction(line):
    parts = line.split(' through ')
    first_part = parts[0].split(' ')
    start = [int(point) for point in first_part.pop().split(',')]
    finish = [int(point) for point in parts[1].split(',')]
    move = first_part[-1]
    return {
        'start':start
        ,'finish':finish
        ,'move':move
    }

def do_instructions(puzzle):
    lits = []
    puzzle = [puzzle[3],puzzle[4]]#for test
    for piece in puzzle:
        piece_data = parse_instruction(piece)
        for current_x in range(piece_data['start'][0],piece_data['finish'][0]):
            current_y = piece_data['start'][1]
            if [current_x,current_y] not in lits and (piece_data['move']=='on' or piece_data['move']=='toggle'):
                print([current_x,current_y])
                lits.append([current_x,current_y])
            elif [current_x,current_y] in lits and (piece_data['move']=='off' or piece_data['move']=='toggle'):
                print([current_x,current_y])
                lits.remove([current_x,current_y])
            for current_y in range(piece_data['start'][1],piece_data['finish'][1]):
                if [current_x,current_y] not in lits and (piece_data['move']=='on' or piece_data['move']=='toggle'):
                    lits.append([current_x,current_y])
                elif [current_x,current_y] in lits and (piece_data['move']=='off' or piece_data['move']=='toggle'):
                    lits.remove([current_x,current_y])
    return lits
print(do_instructions(lines))