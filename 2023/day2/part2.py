import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(2,2023)

lines = puzzle_input.split('\n')

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

def multiply_least_possible(puzzle):
    result = 0
    for piece in puzzle:
        parsed_data = parse_data(piece)
        most_red = 0
        most_green = 0
        most_blue = 0
        for game in parsed_data['games']:
            for game_part in game:
                #print(game_part)
                if game_part[1]=='blue' and game_part[0]>most_blue:
                    most_blue = game_part[0]
                if game_part[1]=='green' and game_part[0]>most_green:
                    most_green = game_part[0]
                if game_part[1]=='red' and game_part[0]>most_red:
                    most_red = game_part[0]
        result += most_blue*most_green*most_red
    return result

print(multiply_least_possible(lines))