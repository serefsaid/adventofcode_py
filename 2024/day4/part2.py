import sys
sys.path.insert(0, '../adventofcode_py')

import fetch_puzzle

puzzle_input = fetch_puzzle.get_puzzle_input(4,2024)
lines = puzzle_input.split('\n')
total_xmas_count = 0
line_count = len(lines)#for exceed control
line_len = len(lines[0])#for exceed control
for line_idx,line in enumerate(lines):
    for ch_idx,ch in enumerate(line):
        if ch=='A':
            rows_enough_upper = 1<=line_idx
            rows_enough_lower = line_idx<(line_count-1)
            columns_enough_left = 1<=ch_idx
            columns_enough_right = ch_idx<(line_len-1)
            if rows_enough_lower and rows_enough_upper and columns_enough_left and columns_enough_right:
                if (
                    (lines[line_idx-1][ch_idx-1]=="M" and lines[line_idx-1][ch_idx+1]=="M" and lines[line_idx+1][ch_idx-1]=="S" and lines[line_idx+1][ch_idx+1]=="S")#MM SS 
                    or (lines[line_idx-1][ch_idx-1]=="M" and lines[line_idx-1][ch_idx+1]=="S" and lines[line_idx+1][ch_idx-1]=="M" and lines[line_idx+1][ch_idx+1]=="S")#MS MS 
                    or (lines[line_idx-1][ch_idx-1]=="S" and lines[line_idx-1][ch_idx+1]=="S" and lines[line_idx+1][ch_idx-1]=="M" and lines[line_idx+1][ch_idx+1]=="M")#SS MM 
                    or (lines[line_idx-1][ch_idx-1]=="S" and lines[line_idx-1][ch_idx+1]=="M" and lines[line_idx+1][ch_idx-1]=="S" and lines[line_idx+1][ch_idx+1]=="M")#SM SM 
                    ):
                    total_xmas_count+=1
            
            

print(total_xmas_count)
#python 2024/day4/part2.py