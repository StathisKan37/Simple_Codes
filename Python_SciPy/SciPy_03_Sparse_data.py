import numpy as np
from scipy.sparse import csr_matrix

# Defining a matrix
matrix_1 = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

# Printing all the non-zero values of matrix_1
print(f'All non-zeros:\n{csr_matrix(matrix_1)}')

# Counting the non-zero values
print(f'Matrix 1 has {csr_matrix(matrix_1).count_nonzero()} non-zero values')

# Viewing the non-zero values with data property
print(f'All non-zeros:\n{csr_matrix(matrix_1).data}')

# SOURCE:
# https://www.w3schools.com/python/scipy/scipy_sparse_data.php
