import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(3,2024)


import re
from typing import List, Dict, Union

_PATTERN = re.compile(r'mul\((-?\d+(?:\.\d+)?),(-?\d+(?:\.\d+)?)\)')

def find_mul_expressions(text):
    results = []
    for m in _PATTERN.finditer(text):
        results.append(m.group(0))
    return results

def multiplier(text):
    splitted_text = text.split('(')[1].split(')')[0].split(',')
    return int(splitted_text[0])*int(splitted_text[1])

mul_expressions = find_mul_expressions(puzzle_input)

total = 0
for me in mul_expressions:
    mul_result = multiplier(me)
    total += mul_result

print(total)
#python 2024/day3/part1.py