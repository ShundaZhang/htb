import gensim.downloader as api

# Load the GloVe model
glove_model = api.load("glove-twitter-25")

def find_analogy(X, Y, Z):
    try:
        result = glove_model.most_similar(positive=[Y, Z], negative=[X], topn=1)
        return result[0][0]
    except KeyError as e:
        return str(e)

# Example analogy
X = "non-mainstream"
Y = "efl"
Z = "battery-powered"
print(f"Like {X} is to {Y}, {Z} is to {find_analogy(X, Y, Z)}")

