import gensim.downloader as api

# 加载 GloVe 模型（通过 Gensim）
glove_model = api.load("glove-twitter-25")

# 使用 most_similar 方法

result = glove_model.most_similar('eme')
print(result)

