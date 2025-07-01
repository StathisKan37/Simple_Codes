import numpy
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
from sklearn.cluster import AgglomerativeClustering

# Two arrays to represent X axis and Y axis
array_x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
array_y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# Scatter plot to visualize the raw data points
plt.scatter(array_x, array_y)
plt.title('Original Data Points')
plt.show() 

# Combining X and Y coordinates into a list of tuples for clustering
data = list(zip(array_x, array_y))
print(f'Combined data:\n{data}')

# Clustering using Ward's method and Euclidean distance
linkage_data = linkage(data, method='ward', metric='euclidean')

# Plot a dendrogram to show the hierarchical clustering structure
dendrogram(linkage_data)
plt.title('Dendrogram')
plt.show()

# SOURCE:
# https://www.w3schools.com/python/python_ml_hierarchial_clustering.asp
