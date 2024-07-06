import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import MDS, TSNE

# 读取npy文件
distance_matrix_path = 'token_embeddings.npz'  # 修改为实际路径
distance_matrix = np.load(distance_matrix_path)['embeddings']

# 检查矩阵的形状
print(f"Distance matrix shape: {distance_matrix.shape}")

# 可视化距离矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(distance_matrix, cmap='viridis')
plt.title('Distance Matrix Heatmap')
plt.show()

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

# 2. 使用t-SNE进行降维
tsne = TSNE(n_components=2, metric='precomputed', random_state=42)
tsne_embedding = tsne.fit_transform(distance_matrix)

print(f"t-SNE embedded points shape: {tsne_embedding.shape}")

# 可视化t-SNE结果
plt.figure(figsize=(10, 7))
plt.scatter(tsne_embedding[:, 0], tsne_embedding[:, 1], cmap='viridis')
plt.title('t-SNE Embedding')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.show()

# 可选：保存降维结果
np.save('mds_embedding.npy', mds_embedding)
np.save('tsne_embedding.npy', tsne_embedding)

