import numpy as np

# Mathematics
A=np.array([1,2,3,4,5])

# Addition (+2)
print(A + 2)
# Substraction (-2)
print(A - 2)
# Multiplication (x2)
print(A * 2)
# Division (/2)
print(A / 2)
# Power (^2)
print(A ** 2)
# Trigonometry
print(np.sin(A))
print(np.cos(A))

# Linear algebra:
B1=np.full((2,3), 2)
B2=np.full((3,2), 2)

# Multiplication of 2 matrixes
print(np.matmul(B1,B2))

# Printing the determinant
C=np.identity(3)
print(np.linalg.det(C))
