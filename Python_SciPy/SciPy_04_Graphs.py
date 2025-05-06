import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order

# A graph with elements A, B and C:
# A & B are connected with weight 1
# A & C are connected with weight 2
# C & B are not connected

# Defining an matrix
#    A B C
# A:[0 1 2]  
# B:[1 0 0]
# C:[2 0 0]
matrix_np = np.array([[0, 1, 2],[1, 0, 0],[2, 0, 0]])

# Converting the matrix to a sparse CSR format
matrix_csr = csr_matrix(matrix_np)

# Analizing the graph
print('--Connected components--')
n_components, labels = connected_components(matrix_csr)
print(f'Number of components: {n_components}')
print(f'Nodes A,B,C belong to components: {labels}')

print('--Shortest paths from node 0--')
print('--Dijkstra method--')
distance_1, predecessors_1 = dijkstra(matrix_csr, return_predecessors=True, indices=0)
print(f'Dijkstra distances from node 0: {distance_1}')
print(f'Dijkstra predecessors from node 0: {predecessors_1}')

print('--Floyd Warshall method--')
distance_2, predecessors_2 = floyd_warshall(matrix_csr, return_predecessors=True)
print(f'Distance matrix:\n{distance_2}')
print(f'Predecessor matrix:\n{predecessors_2}')

print('--Bellman Ford method--')
distance_3, predecessors_3 = bellman_ford(matrix_csr, return_predecessors=True, indices=0)
print(f'Distance array: {distance_3}')
print(f'Predecessor array: {predecessors_3}')

print('--Depth First Order--')
order_1, predecessors_4 = depth_first_order(matrix_csr, 1)
print(f'Order: {order_1}')
print(f'Predecessors: {predecessors_4}')

print('--Breadth First Order--')
order_2, predecessors_5 = breadth_first_order(matrix_csr, 1)
print(f'Order: {order_2}')
print(f'Predecessors: {predecessors_5}')

# SOURCE:
# https://www.w3schools.com/python/scipy/scipy_graphs.php
