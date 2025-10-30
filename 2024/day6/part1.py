import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(6,2024)
lines = puzzle_input.split('\n')

def get_start(lines):
    for y,line in enumerate(lines):
        for x,ch in enumerate(line):
            if ch=='^':
                return x,y

def get_next_location(current_position,rotation,old_positions):
    row_count = len(lines)
    col_count = len(lines[0])
    current_x = current_position[0]
    current_y = current_position[1]
    if rotation=='^':
        for y in range(1,current_y+1):
            if lines[current_y-y][current_x]=="#":
                return (current_x),(current_y-y+1),'>',old_positions
            else:
                old_positions.append(((current_x),(current_y-y)))
        return None,None,None,old_positions
    elif rotation=='>':
        for x in range(1,col_count-current_x):
            if lines[current_y][current_x+x]=="#":
                return (current_x+x-1),(current_y),'v',old_positions
            else:
                old_positions.append(((current_x+x),(current_y)))
        return None,None,None,old_positions
    elif rotation=='v':
        for y in range(1,row_count-current_y):
            if lines[current_y+y][current_x]=="#":
                return (current_x),(current_y+y-1),'<',old_positions
            else:
                old_positions.append(((current_x),(current_y+y)))
        return None,None,None,old_positions
    elif rotation=='<':
        for x in range(1,current_x+1):
            if lines[current_y][current_x-x]=="#":
                return (current_x-x+1),(current_y),'^',old_positions
            else:
                old_positions.append(((current_x-x),(current_y)))
        return None,None,None,old_positions
    return None,None,None,old_positions


start = get_start(lines)
positions = [start]
current_pos = start
rotation = '^'
while True:
    next_x, next_y, rotation, positions = get_next_location(current_pos,rotation,positions)
    if not (next_x and next_y):
        break
    current_pos = (next_x, next_y)


distinct_areas = list(set(positions))
distinct_area_count = len(distinct_areas)
print(distinct_area_count)
#python 2024/day6/part1.py