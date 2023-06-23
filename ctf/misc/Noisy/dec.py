import numpy as np
from scipy.io.wavfile import read

sample_rate, audio_data = read("encrypted.wav")
print(sample_rate)
print(audio_data)
