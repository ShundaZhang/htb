import numpy as np
from scipy.io.wavfile import write

from secret import flag


N = 1_000_000
T = .0001

x = np.linspace(0.0, N*T, N, endpoint=False)
final_waveform = 0

count_used = dict()

for i, c in enumerate(flag):
    count_used[c] = count_used.get(c, 0) + 1
    multiplier = .1 * c * (4**(count_used[c]-1))
    final_waveform += (i+1) * np.sin(2 * np.pi * x * multiplier)

write("encrypted.wav", 20_000_000, final_waveform)
