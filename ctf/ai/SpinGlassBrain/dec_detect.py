import numpy as np
import matplotlib.pyplot as plt

# 加载权重矩阵
weights = np.load("weights.npy")

# 定义从权重矩阵中提取模式的函数
def extract_patterns(weights, num_patterns=16, pattern_size=(80, 80)):
    num_neurons = pattern_size[0] * pattern_size[1]
    assert weights.shape == (num_neurons, num_neurons), "Size not match!"

    patterns = np.zeros((num_patterns, num_neurons))
    for i in range(num_patterns):
        # 使用固定的初始化向量来确保模式顺序
        pattern = np.ones(num_neurons)
        pattern[:i] = -1  # 设置不同的初始状态
        prev_pattern = np.zeros_like(pattern)
        while not np.array_equal(pattern, prev_pattern):
            prev_pattern = pattern.copy()
            pattern = np.sign(np.dot(weights, pattern))
        patterns[i] = pattern

    return patterns.reshape((num_patterns, *pattern_size))

def visualize_patterns(patterns, pattern_size=(80, 80)):
    num_patterns = patterns.shape[0]
    grid_size = int(np.ceil(np.sqrt(num_patterns)))
    fig, axs = plt.subplots(grid_size, grid_size, figsize=(12, 12))
    plt.subplots_adjust(wspace=0, hspace=0)
    axs = axs.flatten()
    for i, ax in enumerate(axs):
        if i < num_patterns:
            ax.imshow(patterns[i].reshape(pattern_size), cmap="gray", aspect="auto")
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()

# 提取模式
patterns = extract_patterns(weights)

# 可视化提取的模式
visualize_patterns(patterns)

