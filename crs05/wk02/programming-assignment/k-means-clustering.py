"""Cluster items using k-mean algorithm."""

from sklearn.cluster import KMeans
import numpy as np

# X = np.array([[1, 2], [1, 4], [1, 0],
# ...               [4, 2], [4, 4], [4, 0]])
# kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
# kmeans.labels_
# array([0, 0, 0, 1, 1, 1], dtype=int32)
# kmeans.predict([[0, 0], [4, 4]])
# array([0, 1], dtype=int32)
# kmeans.cluster_centers_
# array([[ 1.,  2.],
#       [ 4.,  2.]])

# Read places from text and print basic description
places = np.loadtxt(fname="./source/places.txt", delimiter=",")
print("Places has shape ({}, {})".format(*places.shape))
print("First five rows:")
print(places[:5,])

# Set k-means clustering parameters
kmeans = KMeans(n_clusters=3, random_state=42)

# Find clusters in places; adds row index to returned labels
kmeans.fit(places)
clusteredPlaces = [[i, v] for i, v in enumerate(kmeans.predict(places))]

# Output clusters to text
np.savetxt(fname="./output/clustered-places.txt", X=clusteredPlaces, fmt="%.1i")