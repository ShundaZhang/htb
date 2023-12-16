from pwn import *
import re
from stockfish import Stockfish

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


ip, port = "159.65.20.166", 30186
io = remote(ip, port)

engine_path = './stockfish-ubuntu-x86-64-avx2'
stockfish = Stockfish(engine_path)

io.recvline()


for _ in range(50):
    given_string = io.recvuntil("What's the best move?")

    print(given_string.decode('utf-8'))

    given_string = given_string.decode('utf-8').split('\n')[3:-2]

    given_string = [re.sub(r'\x1b.*?m', '', line) for line in given_string]

    given_string = [line[2:-2] for line in given_string]

    for line in given_string:
        print(line)

    fen_lines = []
    for line in given_string:
        fen_line = ''.join([pieces_mapping[char] for char in line])
        fen_line = fen_line.replace('  ', '1')
        fen_line = fen_line.replace(' ', '')
        fen_lines.append(fen_line)

    result = '/'.join(fen_lines)
    result = compress_string(result)
    print(result)
    result = result + " w - - 0 1"

    stockfish.set_fen_position(result)
    best_move = stockfish.get_best_move()
    print("Best move:", best_move)
    io.sendline(best_move)

buf = io.recvuntil('HTB{')
print(buf)
print(io.recvline())

#HTB{th4nk_g0d_f0r_st0ckf1sh}
