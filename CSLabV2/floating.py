def shift_left(str):
    return str[1:len(str)] + '0'

def shift_right(str):
    return '0' + str[:len(str) - 1]

def logical_xor(str1, str2):
    return bool(str1) ^ bool(str2)

def to_n_bit(bin_number, n=32):
    temp_str = ''
    while len(temp_str + bin_number) < n:
        temp_str += '0'
    
    return temp_str + bin_number

def multiply(multiplicand, multiplier):
    bin_multiplicand = to_n_bit(bin(multiplicand).lstrip('0b'), n=32)
    print('Multiplicand: ' + bin_multiplicand)
    
    bin_multiplier = to_n_bit(bin(multiplier).lstrip('0b'), n=32)
    print('Multiplier: ' + bin_multiplier)
    
    bin_product = to_n_bit(bin(0).lstrip('0b'), n=64)
    print('Initializing register: ' + bin_product)
    print()
    
    for i in range(0, 32):
        if bin_multiplier[len(bin_multiplier) - 1] == '1':
            bin_product = bin_add(bin_multiplicand, bin_product)
        bin_multiplicand = shift_left(bin_multiplicand)
        bin_multiplier = shift_right(bin_multiplier)
        print()

    return int(bin_product, 2)
