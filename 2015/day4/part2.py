import hashlib

puzzle_input = 'bgvyzdsv'

def find_code_to_hash(puzzle):
    for number in range(0,9999999):
        number = create_hexadecimal(number)
        code = puzzle + str(number)
        bayt_veri = bytes(code, 'utf-8')
        code = hashlib.md5(bayt_veri).hexdigest()
        if code[:6]=='000000':
            break
    return number#checked the code if range is enough to find hash with six zero. then increased the range

def create_hexadecimal(number):
    length = len(str(number))
    zero_count = 6-length
    newNumber = ''
    for zero in range(0,zero_count):
        newNumber+='0'
    newNumber += str(number)
    return newNumber

print(find_code_to_hash(puzzle_input))