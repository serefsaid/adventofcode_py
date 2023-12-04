import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(4,2023)

lines = puzzle_input.split('\n')


def parse(line):
    game_part = line.split(':')[1]
    seperated = game_part.split('|')
    winning_numbers = seperated[0].split()
    my_numbers = seperated[1].split()
    result = {
        "winning_numbers":winning_numbers
        ,"my_numbers":my_numbers
    }
    return result

def calculate_winnings(lines):
    all_counts = []
    for line in lines:
        data = parse(line)
        match_count = 0
        for winning_number in data['winning_numbers']:
            if winning_number in data['my_numbers']:
                match_count +=1
        all_counts.append([match_count,1])#one stands for card copy count
    return all_counts

def calculate_cards(winnings):
    index = 0
    card_sum = 0
    for winning in winnings:
        matching_number = winning[0]
        cart_copies = winning[1]#original included
        start_copy = index+1
        finish_copy = start_copy+matching_number
        for copy in range(start_copy,finish_copy):
            winnings[copy][1]+=cart_copies#increase copies
        card_sum += cart_copies
        index+=1
    return card_sum

winnings = calculate_winnings(lines)

print(calculate_cards(winnings))