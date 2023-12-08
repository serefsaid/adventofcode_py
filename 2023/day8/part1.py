import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(8,2023)

lines = puzzle_input.split('\n')
del lines[1]#to remove blank line

instructions,*maps = lines
#parsing puzzle starts
maps = [piece.split(' = ') for piece in maps]
maps = {piece[0]:piece[1].replace('(','').replace(')','').split(', ') for piece in maps}
#parsing puzzle ends

current_map = maps['AAA']
step_count = 1

instructions_clone = instructions[:]
found = False
while not found:#till find zzz key
    instruction = instructions_clone[0]
    instructions_clone = instructions_clone[1:]
    if instruction=='L':
        map_key = current_map[0]
    else:#'R'
        map_key = current_map[1]

    if map_key =='ZZZ':
        found = True
    else:
        current_map = maps[map_key]
        step_count+=1
    
    if len(instructions_clone)==0:#recreate instructions
        instructions_clone=instructions[:]
print(step_count)