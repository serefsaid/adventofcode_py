import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(2,2024)
lines = puzzle_input.split('\n')

safe_reports = 0
for idx in range(0,len(lines)):
    numbers = list(map(int,lines[idx].split()))
    for x in range(0,2):
        if x==1:
            tolerated = True
            numbers.pop(0)
        else:
            tolerated = False
        increase = numbers[0]<numbers[1]
        decrease = numbers[0]>numbers[1]
        if not increase and not decrease:
            if tolerated:
                continue
            else:
                tolerated = True
        to_report = True
        for idx in range(0,len(numbers)-1): 
            num = numbers[idx]
            next_num = numbers[idx+1]
            if increase:
                diff = next_num - num
            elif decrease:
                diff = num - next_num

            if diff>3 or diff<1 and tolerated:
                to_report = False
            elif diff>3 or diff<1:
                tolerated = True
        if to_report:
            safe_reports += 1
            break


            

print(safe_reports)
#python 2024/day2/part2.py