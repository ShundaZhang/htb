import numpy as np

def extract_patterns(weights, num_patterns=16, pattern_size=(80, 80)):
    """
    从权重矩阵中提取存储的模式。
    
    参数:
    - weights: 权重矩阵，形状为 (6400, 6400)
    - num_patterns: 需要提取的模式数量
    - pattern_size: 每个模式的大小，默认为 (80, 80)
    
    返回:
    - patterns: 提取的模式数组，形状为 (num_patterns, 80, 80)
    """
    num_neurons = pattern_size[0] * pattern_size[1]
    assert weights.shape == (num_neurons, num_neurons), "权重矩阵大小不匹配"
    
    patterns = np.zeros((num_patterns, num_neurons))
    
    for i in range(num_patterns):
        # 初始化随机模式
        pattern = np.random.choice([-1, 1], num_neurons)
        prev_pattern = np.zeros_like(pattern)
        
        # 迭代更新模式，直到收敛
        while not np.array_equal(pattern, prev_pattern):
            prev_pattern = pattern.copy()
            pattern = np.sign(np.dot(weights, pattern))
        
        patterns[i] = pattern
    
    return patterns.reshape((num_patterns, *pattern_size))

# 加载权重矩阵
weights = np.load("weights.npy")

# 提取模式
np.random.seed(0)
patterns = extract_patterns(weights)

# 初始化flag数组
flag = np.zeros((16, 80, 80))

# 将提取的模式存储在flag数组中
for i in range(16):
    flag[i] = patterns[i]

# 绘制flag数组
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4, 4, figsize=(14, 14))
plt.subplots_adjust(wspace=0.1, hspace=0.1)
axs = axs.flatten()
for i, ax in enumerate(axs):
    ax.imshow(flag[i], cmap="gray", aspect="auto")
    ax.set_title(f"Pattern {i+1}")
    ax.set_xticks([])
    ax.set_yticks([])
plt.show()

