import numpy as np

# A: 4x4 matrix full of zeros
# Default dtype is float64
A=np.zeros((4,4))

# B: 4x4 matrix full of ones
B=np.ones((4,4))

# C: 4x4 matrix full of 5, or any number
# 16 bits intigers
C=np.full((4,4), 5, dtype='int16')

# D: a matrix full of 8, same size of C
D=np.full_like(C,8)

# E: 4x4 matrix full of random floats
E=np.random.rand(4,4)

# F: a matrix full of random floats, same size as E
F=np.random.random_sample(E.size)

# G: 4X4 matrix full of random integers from 0 to 10
G=np.random.randint(0,10, size=(4,4))

# H: 4X4 identity matrix
# Diagonal elements are 1, others are 0
H=np.identity(4)

# Excersice: Try to make the matrix:
# [1 1 1 1 1]
# [1 0 0 0 1]
# [1 0 9 0 1]
# [1 0 0 0 1]
# [1 1 1 1 1]
K=np.ones((5,5))
L=np.zeros((3,3))
L[1,1]=9
K[1:4,1:4]=L
print(K)
