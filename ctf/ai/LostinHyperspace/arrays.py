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

# 获取 tokens 和 embeddings
tokens = data['tokens']
embeddings = data['embeddings']

# 检查嵌入维度
print("Embeddings shape:", embeddings.shape)  # 应该是 (110, 512)

from sklearn.metrics.pairwise import cosine_similarity

# 取出第一个和第二个 token 的嵌入向量
vector1 = embeddings[0]
vector2 = embeddings[1]

# 计算余弦相似度
similarity = cosine_similarity([vector1], [vector2])
print("Cosine Similarity:", similarity[0][0])

from sklearn.cluster import KMeans

# 聚类
kmeans = KMeans(n_clusters=5, random_state=0).fit(embeddings)

# 查看聚类结果
print("Cluster centers:", kmeans.cluster_centers_)
print("Labels:", kmeans.labels_)

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# 降维
tsne = TSNE(n_components=2, random_state=0)
embeddings_2d = tsne.fit_transform(embeddings)

# 可视化
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], c=kmeans.labels_)
plt.colorbar()
plt.show()

