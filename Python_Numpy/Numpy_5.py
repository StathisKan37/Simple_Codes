import numpy as np

# Reorganising arrays
A=np.array([[0,1,2,3],[4,5,6,7]])

# Reshaping the matrix A
print(A.reshape((1,8)))
print(A.reshape((4,2)))
print(A.reshape((2,2,2)))

# Verticaly stacking vectors
B1=np.array([0,1,2,3])
B2=np.array([4,5,6,7])
print("Vertical stack:\n", np.vstack([B1,B2]))

# Horizontal stacking vectors
C1=np.array([[0,1],[4,5]])
C2=np.array([[2,3],[6,7]])
print("Horizontal stack:\n", np.hstack([C1,C2]))
