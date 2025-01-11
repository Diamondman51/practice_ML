# This is descriptor of data
class ReadIntY:
    def __set_name__(self, owner, name):
        self.name = '_y'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


# This is descriptor of non-data (Without __set__ dunder method)
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


# This is data descriptor
class Integer:
    @classmethod
    def verify_coord(cls, value):
        if type(value) != int:
            raise TypeError('Coordinate must be integer!!!')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)


class Point3d:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()
    yr = ReadIntY()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3d(3, 4, 5)
# This is priority of data-descriptor
p.__dict__['yr'] = 5
print(p.__dict__)
print(p.y, p.yr)

# This is priority of non-data descriptor. If we add local variable as shown on the next example the output changes
print(p.__dict__)
print(p.x, p.xr)

# This is priority of local variable
p.__dict__['xr'] = 5
print(p.__dict__)
print(p.x, p.xr)


# TODO Defining priorities of treating to the class variables
# 1. Data-descriptor First place
# 2. Local variable Second place
# 3. Non data-descriptor Third place


from gensim import downloader
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

# Load the GloVe model
model = downloader.load("glove-wiki-gigaword-50")

# Define the target word and its similar words
word = "tower"
similar_words = model.most_similar(word, topn=10)  # Get top 10 similar words
words = [word] + [w for w, _ in similar_words]

# Get the word vectors
vectors = np.array([model[w] for w in words])  # Convert to a NumPy array

# Reduce dimensions to 2D using t-SNE
tsne = TSNE(n_components=2, random_state=42, perplexity=5)
reduced_vectors = tsne.fit_transform(vectors)

# Plot the words in 2D space
plt.figure(figsize=(8, 6))
plt.scatter(reduced_vectors[:, 0], reduced_vectors[:, 1], color='blue')

# Annotate each point with its word
for i, w in enumerate(words):
    plt.annotate(w, (reduced_vectors[i, 0], reduced_vectors[i, 1]), fontsize=20)

plt.title("Word Embeddings Visualization")
plt.xlabel("Dimension 1")
plt.ylabel("Dimension 2")
plt.grid(True)
plt.show()
