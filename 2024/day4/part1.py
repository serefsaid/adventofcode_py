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
        if ch=='X':
            rows_enough_upper = 3<=line_idx
            rows_enough_lower = line_idx<(line_count-3)
            columns_enough_left = 3<=ch_idx
            columns_enough_right = ch_idx<(line_len-3)
            if columns_enough_right:
                if (line[ch_idx+1]=="M" and line[ch_idx+2]=="A" and line[ch_idx+3] == "S"):#vertical-right
                    total_xmas_count+=1
            if columns_enough_left:
                if (line[ch_idx-1]=="M" and line[ch_idx-2]=="A" and line[ch_idx-3] == "S"):#vertical-left
                    total_xmas_count+=1
            if rows_enough_lower:
                if (lines[line_idx+1][ch_idx]=="M" and lines[line_idx+2][ch_idx]=="A" and lines[line_idx+3][ch_idx] == "S"):#horizontal-lower
                    total_xmas_count+=1
            if rows_enough_upper:
                if (lines[line_idx-1][ch_idx]=="M" and lines[line_idx-2][ch_idx]=="A" and lines[line_idx-3][ch_idx] == "S"):#horizontal-upper
                    total_xmas_count+=1
            if rows_enough_lower and columns_enough_right:
                if (lines[line_idx+1][ch_idx+1]=="M" and lines[line_idx+2][ch_idx+2]=="A" and lines[line_idx+3][ch_idx+3] == "S"):#crosswise-lower-right
                    total_xmas_count+=1
            if rows_enough_upper and columns_enough_left:
                if (lines[line_idx-1][ch_idx-1]=="M" and lines[line_idx-2][ch_idx-2]=="A" and lines[line_idx-3][ch_idx-3] == "S"):#crosswise-upper-left
                    total_xmas_count+=1
            if rows_enough_lower and columns_enough_left:
                if (lines[line_idx+1][ch_idx-1]=="M" and lines[line_idx+2][ch_idx-2]=="A" and lines[line_idx+3][ch_idx-3] == "S"):#crosswise-lower-left
                    total_xmas_count+=1
            if rows_enough_upper and columns_enough_right:
                if (lines[line_idx-1][ch_idx+1]=="M" and lines[line_idx-2][ch_idx+2]=="A" and lines[line_idx-3][ch_idx+3] == "S"):#crosswise-upper-right
                    total_xmas_count+=1
            
            

print(total_xmas_count)
#python 2024/day4/part1.py