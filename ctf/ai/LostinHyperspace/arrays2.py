import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# 加载NPZ文件
data = np.load('token_embeddings.npz')

# 获取 tokens 和 embeddings
tokens = data['tokens']
embeddings = data['embeddings']


# 使用 KMeans 进行聚类
n_clusters = 5
kmeans = KMeans(n_clusters=n_clusters, random_state=0)
labels = kmeans.fit_predict(embeddings)

# 使用 PCA 将嵌入向量降维到 2D 空间
pca = PCA(n_components=2)
embeddings_pca = pca.fit_transform(embeddings)

# 可视化聚类结果
plt.figure(figsize=(10, 8))
for i in range(n_clusters):
    cluster_points = embeddings_pca[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i}')

# 在降维后的点上标记token值
for i, token in enumerate(tokens):
    plt.text(embeddings_pca[i, 0], embeddings_pca[i, 1], token, fontsize=9, ha='right')

plt.legend()
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('KMeans Clustering of Token Embeddings (PCA)')
plt.show()


# 使用 t-SNE 将嵌入向量降维到 2D 空间
tsne = TSNE(n_components=2, random_state=0)
embeddings_tsne = tsne.fit_transform(embeddings)

# 可视化聚类结果
plt.figure(figsize=(10, 8))
for i in range(n_clusters):
    cluster_points = embeddings_tsne[labels == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], label=f'Cluster {i}')

# 在降维后的点上标记token值
for i, token in enumerate(tokens):
    plt.text(embeddings_pca[i, 0], embeddings_pca[i, 1], token, fontsize=9, ha='right')

plt.legend()
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.title('KMeans Clustering of Token Embeddings (t-SNE)')
plt.show()

