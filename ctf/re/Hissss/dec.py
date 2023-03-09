#Search _MEIPASS2, found pyinstaller
#python3.8 pyinstxtractor.py auth
#uncompyle6 auth.pyc #with errors but actually should work...
#pydisasm auth_extracted/auth.pyc > auth.py.asm

'''
# pydisasm version 6.0.5
# Python bytecode 3.8.0 (3413)
# Disassembled from Python 3.7.5 (default, Dec  9 2021, 17:04:37) 
# [GCC 8.4.0]
# Timestamp in code: 0 (1970-01-01 08:00:00)
# Source code size mod 2**32: 0 bytes
# Method Name:       <module>
# Filename:          auth.py
# Argument count:    0
# Position-only argument count: 0
# Keyword-only arguments: 0
# Number of locals:  0
# Stack size:        4
# Flags:             0x00000040 (NOFREE)
# First Line:        2
# Constants:
#    0: 0
#    1: None
#    2: 'Enter password> '
#    3: 12
#    4: "Sorry! You've entered the wrong password."
#    5: 48
#    6: 11
#    7: '!'
#    8: 7
#    9: 5
#   10: 143
#   11: 4
#   12: 1
#   13: 3
#   14: 30
#   15: 2
#   16: 5610
#   17: 'p'
#   18: 6
#   19: 8
#   20: -46
#   21: 64
#   22: 10
#   23: 166
#   24: 'n'
#   25: 9
#   26: 'Sorry, the password is incorrect.'
#   27: 'Well Done! HTB{'
#   28: '}'
# Names:
#    0: sys
#    1: input
#    2: password
#    3: len
#    4: print
#    5: exit
#    6: ord
#    7: str
  2:           0 LOAD_CONST           (0)
               2 LOAD_CONST           (None)
               4 IMPORT_NAME          (sys)
               6 STORE_NAME           (sys)

  4:           8 LOAD_NAME            (input)
              10 LOAD_CONST           ('Enter password> ')
              12 CALL_FUNCTION        1
              14 STORE_NAME           (password)

  6:          16 LOAD_NAME            (len)
              18 LOAD_NAME            (password)
              20 CALL_FUNCTION        1
              22 LOAD_CONST           (12)
              24 COMPARE_OP           (!=)
              26 POP_JUMP_IF_FALSE    (to 46)

  7:          28 LOAD_NAME            (print)
              30 LOAD_CONST           ("Sorry! You've entered the wrong password.")
              32 CALL_FUNCTION        1
              34 POP_TOP

  8:          36 LOAD_NAME            (sys)
              38 LOAD_METHOD          (exit)
              40 LOAD_CONST           (0)
              42 CALL_METHOD          1
              44 POP_TOP

 10:     >>   46 LOAD_NAME            (ord)
              48 LOAD_NAME            (password)
              50 LOAD_CONST           (0)
              52 BINARY_SUBSCR
              54 CALL_FUNCTION        1
              56 LOAD_CONST           (48)
              58 COMPARE_OP           (!=)
              60 EXTENDED_ARG         (256)
              62 POP_JUMP_IF_TRUE     (to 342)

 11:          64 LOAD_NAME            (password)
              66 LOAD_CONST           (11)
              68 BINARY_SUBSCR
              70 LOAD_CONST           ('!')
              72 COMPARE_OP           (!=)

 10:          74 EXTENDED_ARG         (256)
              76 POP_JUMP_IF_TRUE     (to 342)

 12:          78 LOAD_NAME            (ord)
              80 LOAD_NAME            (password)
              82 LOAD_CONST           (7)
              84 BINARY_SUBSCR
              86 CALL_FUNCTION        1
              88 LOAD_NAME            (ord)
              90 LOAD_NAME            (password)
              92 LOAD_CONST           (5)
              94 BINARY_SUBSCR
              96 CALL_FUNCTION        1
              98 COMPARE_OP           (!=)

 10:         100 EXTENDED_ARG         (256)
             102 POP_JUMP_IF_TRUE     (to 342)

 13:         104 LOAD_CONST           (143)
             106 LOAD_NAME            (ord)
             108 LOAD_NAME            (password)
             110 LOAD_CONST           (0)
             112 BINARY_SUBSCR
             114 CALL_FUNCTION        1
             116 BINARY_SUBTRACT
             118 LOAD_NAME            (ord)
             120 LOAD_NAME            (password)
             122 LOAD_CONST           (4)
             124 BINARY_SUBSCR
             126 CALL_FUNCTION        1
             128 COMPARE_OP           (!=)

 10:         130 EXTENDED_ARG         (256)
             132 POP_JUMP_IF_TRUE     (to 342)

 14:         134 LOAD_NAME            (ord)
             136 LOAD_NAME            (password)
             138 LOAD_CONST           (1)
             140 BINARY_SUBSCR
             142 CALL_FUNCTION        1
             144 LOAD_NAME            (ord)
             146 LOAD_NAME            (password)
             148 LOAD_CONST           (3)
             150 BINARY_SUBSCR
             152 CALL_FUNCTION        1
             154 BINARY_XOR
             156 LOAD_CONST           (30)
             158 COMPARE_OP           (!=)

 10:         160 EXTENDED_ARG         (256)
             162 POP_JUMP_IF_TRUE     (to 342)

 15:         164 LOAD_NAME            (ord)
             166 LOAD_NAME            (password)
             168 LOAD_CONST           (2)
             170 BINARY_SUBSCR
             172 CALL_FUNCTION        1
             174 LOAD_NAME            (ord)
             176 LOAD_NAME            (password)
             178 LOAD_CONST           (3)
             180 BINARY_SUBSCR
             182 CALL_FUNCTION        1
             184 BINARY_MULTIPLY
             186 LOAD_CONST           (5610)
             188 COMPARE_OP           (!=)

 10:         190 EXTENDED_ARG         (256)
             192 POP_JUMP_IF_TRUE     (to 342)

 16:         194 LOAD_NAME            (password)
             196 LOAD_CONST           (1)
             198 BINARY_SUBSCR
             200 LOAD_CONST           ('p')
             202 COMPARE_OP           (!=)

 10:         204 EXTENDED_ARG         (256)
             206 POP_JUMP_IF_TRUE     (to 342)

 17:         208 LOAD_NAME            (ord)
             210 LOAD_NAME            (password)
             212 LOAD_CONST           (6)
             214 BINARY_SUBSCR
             216 CALL_FUNCTION        1
             218 LOAD_NAME            (ord)
             220 LOAD_NAME            (password)
             222 LOAD_CONST           (8)
             224 BINARY_SUBSCR
             226 CALL_FUNCTION        1
             228 BINARY_SUBTRACT
             230 LOAD_CONST           (-46)
             232 COMPARE_OP           (!=)

 10:         234 EXTENDED_ARG         (256)
             236 POP_JUMP_IF_TRUE     (to 342)

 18:         238 LOAD_NAME            (ord)
             240 LOAD_NAME            (password)
             242 LOAD_CONST           (6)
             244 BINARY_SUBSCR
             246 CALL_FUNCTION        1
             248 LOAD_NAME            (ord)
             250 LOAD_NAME            (password)
             252 LOAD_CONST           (7)
             254 BINARY_SUBSCR
             256 CALL_FUNCTION        1
             258 BINARY_XOR
             260 LOAD_CONST           (64)
             262 COMPARE_OP           (!=)

 10:         264 EXTENDED_ARG         (256)
             266 POP_JUMP_IF_TRUE     (to 342)

 19:         268 LOAD_NAME            (ord)
             270 LOAD_NAME            (password)
             272 LOAD_CONST           (10)
             274 BINARY_SUBSCR
             276 CALL_FUNCTION        1
             278 LOAD_NAME            (ord)
             280 LOAD_NAME            (password)
             282 LOAD_CONST           (5)
             284 BINARY_SUBSCR
             286 CALL_FUNCTION        1
             288 BINARY_ADD
             290 LOAD_CONST           (166)
             292 COMPARE_OP           (!=)

 10:         294 EXTENDED_ARG         (256)
             296 POP_JUMP_IF_TRUE     (to 342)

 20:         298 LOAD_NAME            (ord)
             300 LOAD_CONST           ('n')
             302 CALL_FUNCTION        1
             304 LOAD_NAME            (ord)
             306 LOAD_NAME            (password)
             308 LOAD_CONST           (9)
             310 BINARY_SUBSCR
             312 CALL_FUNCTION        1
             314 BINARY_SUBTRACT
             316 LOAD_CONST           (1)
             318 COMPARE_OP           (!=)

 10:         320 EXTENDED_ARG         (256)
             322 POP_JUMP_IF_TRUE     (to 342)

 21:         324 LOAD_NAME            (password)
             326 LOAD_CONST           (10)
             328 BINARY_SUBSCR
             330 LOAD_NAME            (str)
             332 LOAD_CONST           (3)
             334 CALL_FUNCTION        1
             336 COMPARE_OP           (!=)

 10:         338 EXTENDED_ARG         (256)
             340 POP_JUMP_IF_FALSE    (to 352)

 22:     >>  342 LOAD_NAME            (print)
             344 LOAD_CONST           ('Sorry, the password is incorrect.')
             346 CALL_FUNCTION        1
             348 POP_TOP
             350 JUMP_FORWARD         (to 368)

 24:     >>  352 LOAD_NAME            (print)
             354 LOAD_CONST           ('Well Done! HTB{')
             356 LOAD_NAME            (password)
             358 FORMAT_VALUE         0
             360 LOAD_CONST           ('}')
             362 BUILD_STRING         3
             364 CALL_FUNCTION        1
             366 POP_TOP
         >>  368 LOAD_CONST           (None)
             370 RETURN_VALUE
'''

p = [0]*12

p[0] = 48
p[11] = ord('!')
p[4] = 143 - p[0]
p[1] = ord('p')
p[10] = ord('3')
p[9] = ord('n') - 1 
p[5] = 166 - p[10]
p[3] = 30 ^ p[1]
p[7] = p[5]
p[2] = 5610/p[3]
p[6] = p[7] ^ 64
p[8] = p[6] + 46

print 'HTB{'+''.join([chr(i) for i in p])+'}'
