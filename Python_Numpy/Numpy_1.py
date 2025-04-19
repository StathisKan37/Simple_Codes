# Importing the NumPy library for numerical operations
import numpy as np

# Defining a 1D NumPy array with three integer elements
# 'dtype=int16' specifies that each element is a 16-bit integer
A=np.array([1, 2, 3], dtype='int16')

# Defining a 2D NumPy array (matrix) with floating-point numbers
# NumPy automatically assigns an appropriate datatype (default: float64)
B=np.array([[1.1, 1.2, 1.3],[2.1, 2.2, 2.3]])

# Printing the array and the matrix
print("A =",A)
print("B =",B)

# Printing the dimensions
print("Dimensions of A:", A.ndim)
print("Dimensions of B:", B.ndim)

# Printing the shapes
# Shape represents the number of elements in each dimension
print("Shape of A:", A.shape)
print("Shape of B:", B.shape)

# Printing the datatype
print("Datatype of A:", A.dtype)
print("Datatype of B:", B.dtype)

# Printing the number of elements in each array
print("Size of A:", A.size,"items")
print("Size of B:", B.size,"items")

# Printing the total number of bytes used by each array
print("Number of bytes of A:", A.nbytes, "bytes")
print("Number of bytes of B:", B.nbytes, "bytes")
