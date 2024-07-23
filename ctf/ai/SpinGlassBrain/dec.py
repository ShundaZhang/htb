import matplotlib.pyplot as plt
import numpy as np

# 加载权重矩阵
weights = np.load("weights.npy")

# 定义函数从权重矩阵中提取模式
def extract_patterns(weights, num_patterns=128, pattern_size=(80, 80)):
	num_neurons = pattern_size[0] * pattern_size[1]
	assert weights.shape == (num_neurons, num_neurons), "Size not match!"

	patterns = np.zeros((num_patterns, num_neurons))
	for i in range(num_patterns):
		pattern = np.random.choice([-1, 1], num_neurons)
		prev_pattern = np.zeros_like(pattern)
		while not np.array_equal(pattern, prev_pattern):
			prev_pattern = pattern.copy()
			pattern = np.sign(np.dot(weights, pattern))
		patterns[i] = pattern
	
	return patterns.reshape((num_patterns, *pattern_size))

def encode_pattern(key, arr):
	assert(arr.shape == (80, 80))
	X = arr.copy().flatten()
	
	boolean = format(key, '06b')
	for c_ix, c in enumerate(boolean):
		if c == '1':
			X[c_ix] = 1
		else:
			X[c_ix] = -1
	return X

def decode_pattern(arr):
	assert arr.shape == (80, 80)  # 确保输入数组的形状正确
	
	X = arr.copy().flatten()
	boolean = ''
	for c_ix in range(6):
		if X[c_ix] == 1:
			boolean += '1'
		else:
			boolean += '0'
	
	key = int(boolean, 2)  # 将二进制字符串转换回整数
	return key


np.random.seed(0)
patterns = extract_patterns(weights)

# 初始化存储模式的数组
flag = np.zeros((128, 80, 80))

# 提取模式
for i in range(128):
	#pattern = np.zeros((80, 80))
	encoded_pattern = patterns[i]
	index = decode_pattern(patterns[i]) 
	flag[index] = encoded_pattern.reshape(80, 80)

# 绘制模式
fig, axs = plt.subplots(3, 7, figsize=(14, 6))
plt.subplots_adjust(wspace=0, hspace=0)
axs = axs.flatten()
for c, ax in zip(flag, axs):
	ax.imshow(c.reshape(80, 80), cmap="gray", aspect="auto")
for ax in axs:
	ax.set_xticks([])
	ax.set_yticks([])
plt.show()

#HTB{Br41n_d4nc3}
