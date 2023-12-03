import sys
sys.path.insert(0, '../adventofcode')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(3,2015)


def find_gifted_houses_count(puzzle):
    santa_x = 0
    santa_y = 0
    robo_santa_x = 0
    robo_santa_y = 0
    delivered_directions = [[0,0]]
    santas_turn = True
    for direction in puzzle:
        if santas_turn:
            if direction=='^':
                santa_y+=1
            elif direction=='v':
                santa_y-=1
            elif direction=='<':
                santa_x-=1
            elif direction=='>':
                santa_x+=1
            
            if [santa_x,santa_y] not in delivered_directions:
                delivered_directions.append([santa_x,santa_y])
        elif not santas_turn:
            if direction=='^':
                robo_santa_y+=1
            elif direction=='v':
                robo_santa_y-=1
            elif direction=='<':
                robo_santa_x-=1
            elif direction=='>':
                robo_santa_x+=1
            
            if [robo_santa_x,robo_santa_y] not in delivered_directions:
                delivered_directions.append([robo_santa_x,robo_santa_y])

        if santas_turn:
            santas_turn = False
        else:
            santas_turn = True

    return len(delivered_directions)

print(find_gifted_houses_count(puzzle_input))