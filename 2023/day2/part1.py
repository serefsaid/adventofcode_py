import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(2,2023)

lines = puzzle_input.split('\n')

limits = {
    'red_limit' : 12
    ,'green_limit' : 13
    ,'blue_limit' : 14
}

def parse_data(line):
    gameID = int(line.split(':')[0].replace('Game ',''))
    def split_em(games):
        games = games.split(',')
        game_counter = 0
        for game in games:
            games[game_counter] = game.split(' ')
            games[game_counter].remove('')
            games[game_counter][0] = int(games[game_counter][0])
            game_counter+=1
        return games
    games = list(map(split_em,line.split(':')[1].split(';')))
    result = {
        'gameID':gameID
        ,'games':games
    }
    return result

def sum_possible_ids(puzzle):
    possible_ids = []
    for piece in puzzle:
        parsed_data = parse_data(piece)
        error_count = 0
        for game in parsed_data["games"]:
            for game_part in game:
                if (game_part[1]=='blue' and game_part[0]>limits['blue_limit']) or (game_part[1]=='red' and game_part[0]>limits['red_limit']) or (game_part[1]=='green' and game_part[0]>limits['green_limit']):
                    error_count+=1
        if error_count==0:
            possible_ids.append(parsed_data['gameID'])
    return sum(possible_ids)

print(sum_possible_ids(lines))