'''
Python Exe to Py

python3.8 pyinstxtractor.py maze.exe
cd maze.exe_extracted/
uncompyle6 maze.pyc
uncompyle6 maze.pyc > maze.py

cd PYZ-00.pyz_extracted/
uncompyle6 obf_path.pyc > obf_path.py

Or

7z x enc_maze.zip 
with password "Y0u_Ar3_W4lkiNG_t0_Y0uR_D34TH"

python3.9 maze.py

python3.9 maze.py
Look who comes to me :)

Now There are two paths from here. Which path will u choose? => Y0u_St1ll_1N_4_M4z3


G00d!! you could escape the obfuscated path
take this it may help you:

seed(493)
for i in range(300):
    randint(32,125)

Be Careful!!!! the route from here is not safe.

Generate key: python3.9 key.py
python dec2.py
'''

with open('maze', 'rb') as (file):
    content = file.read()
data = bytearray(content)
data = [x for x in data]
#key = [0] * len(data)
key = [64,119,70,106,64,77,96,110,117,75,95,37,117,65,59,111,70,68,62,104,97,116,87,122,108,77,51,75,70,100,61,47,39,110,34,109,97,122,79,117,43,125,34,107,70,43,108,39,112,119,61,47,89,78,44,46,119,44,61,117,112,117,112,62,54,123,109,46,81,73,56,99,88,102,58,71,52,117,56,85,39,122,115,116,121,100,48,57,40,107,92,81,93,70,99,71,67,62,66,62,32,74,92,101,103,103,115,96,61,62,122,75,120,45,63,40,35,121,95,43,64,104,99,118,119,83,55,120,114,44,71,116,99,62,82,47,33,62,116,88,71,103,39,79,49,45,104,120,122,91,93,90,103,92,124,61,74,84,33,97,84,125,115,53,36,79,75,75,88,84,59,97,86,43,113,62,52,107,59,47,53,45,77,67,67,111,54,84,95,73,87,39,108,104,121,102,56,77,71,43,119,114,120,71,91,85,76,68,67,82,41,57,49,52,61,64,54,89,66,102,41,79,52,49,65,46,75,36,98,105,43,37,53,32,93,64,85,46,37,81,119,77,115,74,94,44,104,41,119,101,59,36,49,42,122,58,63,120,33,49,71,77,83,112,81,76,41,115,100,96,49,82,36,49,75,79,93,125,56,44,86,82,55,122,50,63,121,81,47,97,70,36,46,55,98,91,50,104,40,87]
for i in range(0, len(data), 10):
    data[i] = (data[i] + 80) % 256
else:
    for i in range(0, len(data), 10):
        data[i] = (data[i] ^ key[i % len(key)]) % 256
    else:
        with open('dec_maze', 'wb') as (f):
            for b in data:
                f.write(bytes([b]))

