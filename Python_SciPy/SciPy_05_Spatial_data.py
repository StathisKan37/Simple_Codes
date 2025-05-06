import numpy as np
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
# Spatial data refers to data that is represented in a geometric space

# 2 arrays with points
points_1 = np.array([[2,4],[3,4],[3,0],[2,2],[4,1]])
points_2 = np.array([[2,4],[3,4],[3,0],[4,1],[1,2],[5,0],[3,1],[1,2],[0,2]])

# Delaunay triangulation
simplices = Delaunay(points_1).simplices
# Convex hull
hull = ConvexHull(points_2)
hull_points = hull.simplices

# Plot Delaunay triangulation
plt.triplot(points_1[:, 0], points_1[:, 1], simplices)
plt.scatter(points_1[:, 0], points_1[:, 1], color='r')
plt.title("Delaunay Triangulation")
plt.show()

# Plot Convex Hull
plt.scatter(points_2[:, 0], points_2[:, 1])
for simplex in hull_points:
    plt.plot(points_2[simplex, 0], points_2[simplex, 1], 'k-')
plt.title("Convex Hull")
plt.show()

# SOURCE:
# https://www.w3schools.com/python/scipy/scipy_spatial_data.php
