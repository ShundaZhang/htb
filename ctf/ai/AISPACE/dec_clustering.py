import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
from sklearn.manifold import MDS
from sklearn.cluster import KMeans

# 读取npy文件
distance_matrix_path = 'distance_matrix.npy'  # 修改为实际路径
distance_matrix = np.load(distance_matrix_path)

# 检查矩阵的形状
print(f"Distance matrix shape: {distance_matrix.shape}")

# 可视化距离矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(distance_matrix, cmap='viridis')
plt.title('Distance Matrix Heatmap')
plt.show()

# 1. 层次聚类
# 计算层次聚类链接矩阵
linkage_matrix = linkage(distance_matrix, method='complete') #, metric='precomputed')

# 绘制树状图
plt.figure(figsize=(10, 7))
dendrogram(linkage_matrix)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample index')
plt.ylabel('Distance')
plt.show()

# 确定聚类数并分配标签
k = 5  # 修改为需要的聚类数
cluster_labels_hierarchical = fcluster(linkage_matrix, k, criterion='maxclust')

# 查看层次聚类结果
print(f"Hierarchical Clustering Labels: {cluster_labels_hierarchical}")

# 2. K-means 聚类
# 使用多维尺度分析（MDS）将数据映射到低维空间
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
embedded_points = mds.fit_transform(distance_matrix)

print(f"Embedded points shape: {embedded_points.shape}")

# 使用K-means聚类
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(embedded_points)
cluster_labels_kmeans = kmeans.labels_

# 查看K-means聚类结果
print(f"K-means Clustering Labels: {cluster_labels_kmeans}")

# 可视化K-means聚类结果
plt.figure(figsize=(10, 7))
plt.scatter(embedded_points[:, 0], embedded_points[:, 1], c=cluster_labels_kmeans, cmap='viridis')
plt.title('K-means Clustering with MDS')
plt.xlabel('MDS Component 1')
plt.ylabel('MDS Component 2')
plt.show()

# 可选：保存聚类结果
np.save('hierarchical_clustering_labels.npy', cluster_labels_hierarchical)
np.save('kmeans_clustering_labels.npy', cluster_labels_kmeans)

