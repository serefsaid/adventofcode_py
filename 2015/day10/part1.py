puzzle_input = '1321131112'
#111312211331
def find_convertion(part):
    name = part[0]
    quantity = str(len(part))
    return quantity+name

def parse(puzzle):
    answer = ''
    newStr = ''
    old_number = ''
    for number in puzzle:
        if old_number==number or newStr=='':
            newStr += number
        else:
            answer += find_convertion(newStr)
            newStr = number
        old_number = number[:]
    answer += find_convertion(newStr)
    return answer

for i in range(0,40):#change this to 50 for part 2
    puzzle_input = parse(puzzle_input)

print(len(puzzle_input))