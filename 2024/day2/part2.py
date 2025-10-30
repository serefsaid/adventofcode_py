import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(2,2024)
lines = puzzle_input.split('\n')

def is_safe(numbers):
    increase = numbers[0]<numbers[1]
    decrease = numbers[0]>numbers[1]
    to_report = True
    if not increase and not decrease:
        return False
    for idx in range(len(numbers)-1): 
        num = numbers[idx]
        next_num = numbers[idx+1]
        if increase:
            diff = next_num - num
        elif decrease:
            diff = num - next_num

        if diff>3 or diff<1:
            to_report = False
    return to_report

safe_reports = 0
for idx in range(len(lines)):
    numbers = list(map(int,lines[idx].split()))
    if is_safe(numbers):
        safe_reports += 1
    else:
        for x in range(len(numbers)):
            new_numbers = numbers[:x] + numbers[x+1:]
            if is_safe(new_numbers):
                safe_reports += 1
                break
            

print(safe_reports)
#python 2024/day2/part2.py