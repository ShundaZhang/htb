import numpy as np

# 加载NPZ文件
data = np.load('token_embeddings.npz')

# 列出所有数组的名称
print(data.files)  # 输出: ['arr1', 'arr2']

# 访问具体的数组
arr1 = data['tokens']
arr2 = data['embeddings']

# 显示数组内容
print(arr1)
print(arr2)

