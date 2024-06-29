#Ask ChatGPT, try ML analysis one-by-one:
'''
可能用途
聚类分析（Clustering Analysis）：

距离矩阵可以用来进行聚类算法（如K-means、层次聚类等），以确定数据点的分组。
降维（Dimensionality Reduction）：

方法如多维尺度分析（MDS）和t-SNE需要一个距离矩阵来在低维空间中表示数据点。
分类（Classification）：

在K近邻算法（K-NN）中，距离矩阵用于确定测试样本与训练样本之间的距离。
推荐系统（Recommender Systems）：

距离矩阵可以表示用户或物品之间的相似性，用于推荐系统中的协同过滤。
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import MDS, TSNE

# 读取npy文件
distance_matrix_path = 'distance_matrix.npy'  # 修改为实际路径
distance_matrix = np.load(distance_matrix_path)

# 1. 使用多维尺度分析（MDS）进行降维
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
mds_embedding = mds.fit_transform(distance_matrix)

print(f"MDS embedded points shape: {mds_embedding.shape}")

# 可视化MDS结果
plt.figure(figsize=(10, 7))
plt.scatter(mds_embedding[:, 0], mds_embedding[:, 1], cmap='viridis')
plt.title('MDS Embedding')
plt.xlabel('MDS Component 1')
plt.ylabel('MDS Component 2')
plt.show()

#HTB{d1st4nt_spac3}
