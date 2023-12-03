import hashlib

puzzle_input = 'bgvyzdsv'

def find_code_to_hash(puzzle):
    for number in range(0,999999):
        number = create_hexadecimal(number)
        code = puzzle + str(number)
        bayt_veri = bytes(code, 'utf-8')
        code = hashlib.md5(bayt_veri).hexdigest()
        if code[:5]=='00000':
            break
    return number

def create_hexadecimal(number):
    length = len(str(number))
    zero_count = 6-length
    newNumber = ''
    for zero in range(0,zero_count):
        newNumber+='0'
    newNumber += str(number)
    return newNumber

print(find_code_to_hash(puzzle_input))