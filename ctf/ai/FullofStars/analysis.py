import numpy as np
import gzip

# 定义函数来读取和解析数据
def load_data(filename):
    with gzip.open(filename, 'rb') as f:
        data = np.loadtxt(f)
    return data

# 读取 data.npy.gz 和 known_samples.npy.gz
data = load_data("data.npy.gz")
core_data = load_data("known_samples.npy.gz")

# 将两个数据合并
all_data = np.vstack((core_data, data))

# 打印一些基本信息来解析和了解数据
print("Data shape:", data.shape)
print("Core data shape:", core_data.shape)
print("All data shape:", all_data.shape)

# 进一步查看数据内容
print("First few rows of data:", data[:5])
print("First few rows of core_data:", core_data[:5])

