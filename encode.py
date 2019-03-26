from entropy import process_file, get_results
import os

def base64encode(data):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
    
    bit_str = ''
    base64_str = ''
    div24_symb = ''
    
    for byte in data:
        bin_byte = bin(byte).lstrip("0b")
        bin_byte = bin_byte.zfill(8)
        bit_str += bin_byte
    
    while len(bit_str) % 24 != 0:
        div24_symb = '='
        bit_str += '0'

    groups = [bit_str[x:x+6] for x in range(0, len(bit_str), 6)]
    for group in groups:
        base64_str += alphabet[int(group, 2)]

    base64_str += div24_symb

    return base64_str


# file = open('3.txt', encoding="utf8")
# chars, freq, entropy = get_results(file.read())
# for char in chars:
#     print('%s: %i' % (char, chars[char]))

# print('freq: ', freq)
# print('Entropy: ', entropy)
# print(os.path.getsize('1.txt'))


file2 = open('3.txt.xz', 'rb')
chars, freq, entropy = get_results(file2.read())
for char in chars:
    print('%s: %i' % (char, chars[char]))

print('freq: ', freq)
print('Entropy: ', entropy)
print(os.path.getsize('3.txt.xz'))
