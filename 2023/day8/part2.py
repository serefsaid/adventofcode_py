import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(8,2023)

lines = puzzle_input.split('\n')
del lines[1]#to remove blank line
import math
instructions,*maps = lines
#parsing puzzle starts
maps = [piece.split(' = ') for piece in maps]
maps = {piece[0]:piece[1].replace('(','').replace(')','').split(', ') for piece in maps}
#parsing puzzle ends

current_maps = [value for key,value in maps.items() if key[2]=='A']

def new_current_maps(param_keys):
    return [value for key,value in maps.items() if key in param_keys]

instructions_clone = instructions[:]
multipliers = []
for current_map in current_maps:
    found = False
    step_count = 1
    while not found:
        instruction = instructions_clone[0]
        instructions_clone = instructions_clone[1:]
        if instruction=='L':
            map_key = current_map[0]
        else:#'R'
            map_key = current_map[1]


        if map_key[2] =='Z':
            found = True
            multipliers.append(step_count)
        else:
            current_map = maps[map_key]
            step_count+=1
        
        if len(instructions_clone)==0:#recreate instructions
            instructions_clone=instructions[:]
def find_lcm_of_array(arr):
    def lcm(x, y):
        return x * y // math.gcd(x, y)

    lcm_result = arr[0]
    for i in range(1, len(arr)):
        lcm_result = lcm(lcm_result, arr[i])
    return lcm_result
print(find_lcm_of_array(multipliers))
#print(find_lcm_of_array([3,2,5]))
print(multipliers)