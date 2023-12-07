import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(7,2023)

lines = puzzle_input.split('\n')

puzzle = [[piece[0],int(piece[1])] for piece in [line.split() for line in lines]]

def order(puzzle):
    card_priority = {'A':1, 'K':2, 'Q':3, 'J':4, 'T':5, '9':6, '8':7, '7':8, '6':9, '5':10, '4':11, '3':12,'2':13}#strongest to weakest
    ranks = []
    for piece in puzzle:
        char_count = 0
        char_quantities = []
        last_char = ''
        for char in piece[0]:
            char_quantities.append(card_priority[char])
            if last_char!=char:
                char_count+=1
            last_char = char
        hand = [char_count,piece[1],char_quantities]
        ranks.append(hand)
    ranks.sort(key=lambda x: (x[0], x[2][0], x[2][1], x[2][2], x[2][3], x[2][4]),reverse=True)
    rank_index = 1
    total_winnigs=0
    for rank in ranks:
        total_winnigs += rank[1]*rank_index
        rank_index += 1
    return total_winnigs

print(order(puzzle))