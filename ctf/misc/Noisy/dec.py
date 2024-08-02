import numpy as np
from scipy.io.wavfile import read
from scipy.fft import fft

# Read the waveform from the WAV file
rate, data = read('encrypted.wav')

# Perform FFT to get the frequency components
N = len(data)
yf = fft(data)
xf = np.fft.fftfreq(N, 1 / rate)

# Consider only positive frequencies
positive_xf = xf[:N // 2]
positive_yf = np.abs(yf[:N // 2])

# Define the threshold for significant frequencies
threshold = np.max(positive_yf) * 0  # Adjust as needed

# Define the function to get the character from the frequency
def get_char_from_freq(freq, count_used):
    for c in range(256):
        multiplier = 0.1 * c * (4 ** (count_used[c] - 1))
        if np.isclose(freq, multiplier, atol=1e-2):
            return c
    return None

# Initialize the dictionary to track how many times each character has been used
count_used = {i: 0 for i in range(256)}
flag = []

# Iterate through significant frequencies
for i in range(len(positive_xf)):
    if positive_yf[i] > threshold:  # Consider only significant frequencies
        freq = positive_xf[i]
        char = get_char_from_freq(freq, count_used)
        if char is not None:
            flag.append(char)
            count_used[char] += 1

# Convert the flag list to a byte string
flag = bytes(flag)
print(flag.decode())

