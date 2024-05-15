import numpy as np
from scipy.io.wavfile import read

sample_rate, audio_data = read("encrypted.wav")
print(sample_rate)
print(audio_data)

import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# 读取 WAV 文件
sample_rate, data = read('encrypted.wav')

# 计算时间轴
N = len(data)
T = 1 / sample_rate
x = np.linspace(0.0, N*T, N, endpoint=False)

# 数据预处理
data = data / np.max(np.abs(data))  # 归一化

# 使用傅里叶变换找出频率成分
frequencies = np.fft.fftfreq(N, T)
fft_values = np.fft.fft(data)

# 取绝对值并排序，获取主要频率成分
fft_magnitudes = np.abs(fft_values)
indices = np.argsort(-fft_magnitudes)  # 从大到小排序
primary_frequencies = frequencies[indices]

# 解析每个字符的信息
flag_chars = []
char_count = {}
for i, freq in enumerate(primary_frequencies):
    if freq <= 0:
        continue  # 只考虑正频率

    # 尝试计算字符及其次数
    approximate_char = int(freq / 0.1)
    if approximate_char < 32 or approximate_char > 126:
        continue  # 过滤掉非打印字符的频率

    char = chr(approximate_char)

    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

    expected_freq = .1 * ord(char) * (4**(char_count[char]-1))

    # 判断这个频率是否确实对应这个字符的多次出现情况
    if np.isclose(freq, expected_freq, atol=0.1):
        flag_chars.append(char)

# 组合解析出的字符
decoded_flag = ''.join(flag_chars)
print("Decoded flag:", decoded_flag)

