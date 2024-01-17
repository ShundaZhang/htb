import itertools
import math

n = 72741423208033405403492275698762968936514657314823442485453559870105200118330405900858299998747406127848670334407387228444029070060538220448699667905891284937839901536444798774307744865631349770845980738192442639071823803272283670943732769371979418893953521892212745135191661138195973757608889180051128601323

e = 65537

enc_key = 0x4da0230d2b8b46e3a7065f32c46df019739cc002a208cc37767a82c3e94edfc3440fa4b24a32274e35d5ddceaa33505c4f2a57281c3a5d6d4db3a0dbdbb30dbf373241319ce4a7fdd1780b6bafc86e37d283c9f9787c567434e2fc29c988fb05fd411fe4453ea40eb45fc41a423839b485e238dd2530fba284e9b07a0bba6546

start, end = 2**20, 2**21

# Generate all possible pairs (k1, k2)
pairs = itertools.product(range(start, end), repeat=2)

for k1, k2 in pairs:
    print(f'k1: {k1}, k2: {k2}')
    k = k1 * k2
    if enc_key == pow(k, e, n):
        print('===================================================')
        print(f'k1: {k1}')
        print(f'k2: {k2}')
        print('===================================================')
        break
else:
    print('No solution found.')

