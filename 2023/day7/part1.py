import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(7,2023)

lines = puzzle_input.split('\n')

puzzle = [[piece[0],int(piece[1])] for piece in [line.split() for line in lines]]

from collections import Counter

def hand_type(code):
    game_point = 0
    char_counts = Counter(code)
    values =list(char_counts.values())
    if values.count(5)==1:
        game_point = 1#Five of a kind
    elif values.count(4)==1:
        game_point = 2#Four of a kind
    elif values.count(3)==1 and values.count(2)==1:
        game_point = 3#Full house
    elif values.count(3)==1 and values.count(1)==2:
        game_point = 4#Three of a kind
    elif values.count(2)==2:
        game_point = 5#Two pair
    elif values.count(2)==1 and values.count(1)==3:
        game_point = 6#One pair
    elif values.count(1)==5:
        game_point = 7#High card
    return game_point

def order(puzzle):
    card_priority = {'A':1, 'K':2, 'Q':3, 'J':4, 'T':5, '9':6, '8':7, '7':8, '6':9, '5':10, '4':11, '3':12,'2':13}#strongest to weakest
    ranks = []
    for piece in puzzle:
        char_quantities = []
        for char in piece[0]:
            char_quantities.append(card_priority[char])
        hand = [hand_type(piece[0]),piece[1],char_quantities,piece[0]]
        ranks.append(hand)
    ranks.sort(key=lambda x: (x[0], x[2][0], x[2][1], x[2][2], x[2][3], x[2][4]),reverse=True)
    total_winnigs=0
    rank_index = 1
    for rank in ranks:
        total_winnigs += rank[1]*rank_index
        rank_index+=1
    return total_winnigs

print(order(puzzle))