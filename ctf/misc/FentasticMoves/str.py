import re

def compress_string(input_string):
    result = ''
    count = 0

    for char in input_string:
        if char == '1':
            count += 1
        else:
            if count > 0:
                result += str(count)
                count = 0
            result += char

    if count > 0:
        result += str(count)

    return result

given_string = b"\x1b[48;5;95m                    \x1b[0m\n\x1b[48;5;95m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m \x1b[38;5;16m\xe2\x99\x9a\x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m \x1b[38;5;172m\xe2\x99\x98\x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;95m \x1b[38;5;16m8\x1b[0m\n\x1b[48;5;95m  \x1b[48;5;240m \x1b[38;5;16m\xe2\x99\x9c\x1b[48;5;7m \x1b[38;5;172m\xe2\x99\x98\x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;95m \x1b[38;5;16m7\x1b[0m\n\x1b[48;5;95m  \x1b[48;5;7m \x1b[38;5;172m\xe2\x99\x99\x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;95m \x1b[38;5;16m6\x1b[0m\n\x1b[48;5;95m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m \x1b[38;5;172m\xe2\x99\x95\x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;95m \x1b[38;5;16m5\x1b[0m\n\x1b[48;5;95m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m \x1b[38;5;172m\xe2\x99\x96\x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;95m \x1b[38;5;16m4\x1b[0m\n\x1b[48;5;95m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m \x1b[38;5;172m\xe2\x99\x97\x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m \x1b[38;5;172m\xe2\x99\x94\x1b[48;5;95m \x1b[38;5;16m3\x1b[0m\n\x1b[48;5;95m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;95m \x1b[38;5;16m2\x1b[0m\n\x1b[48;5;95m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m \x1b[38;5;172m\xe2\x99\x97\x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;240m  \x1b[48;5;7m  \x1b[48;5;95m \x1b[38;5;16m1\x1b[0m\n\x1b[48;5;95m  \x1b[38;5;16m a b c d e f g h  \x1b[0m"
print(given_string.decode('utf-8'))

given_string = given_string.decode('utf-8').split('\n')[1:-1]

given_string = [re.sub(r'\x1b.*?m', '', line) for line in given_string]

given_string = [line[2:-2] for line in given_string]

for line in given_string:
    print(line)

pieces_mapping = {
    b'\xe2\x99\x95'.decode('utf-8'): 'Q',
    b'\xe2\x99\x94'.decode('utf-8'): 'K',
    b'\xe2\x99\x96'.decode('utf-8'): 'R',
    b'\xe2\x99\x97'.decode('utf-8'): 'B',
    b'\xe2\x99\x98'.decode('utf-8'): 'N',
    b'\xe2\x99\x99'.decode('utf-8'): 'P',
    b'\xe2\x99\x9b'.decode('utf-8'): 'q',
    b'\xe2\x99\x9a'.decode('utf-8'): 'k',
    b'\xe2\x99\x9c'.decode('utf-8'): 'r',
    b'\xe2\x99\x9d'.decode('utf-8'): 'b',
    b'\xe2\x99\x9e'.decode('utf-8'): 'n',
    b'\xe2\x99\x9f'.decode('utf-8'): 'p',
    ' ': ' '
}

fen_lines = []
for line in given_string:
    fen_line = ''.join([pieces_mapping[char] for char in line])
    fen_line = fen_line.replace('  ', '1')  
    fen_line = fen_line.replace(' ', '')  
    fen_lines.append(fen_line)

result = '/'.join(fen_lines)
result = compress_string(result)
print(result)

