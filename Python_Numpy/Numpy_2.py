import numpy as np

A=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
B=np.array([[[0,1,2,3],[4,5,6,7]],[[8,9,10,11],[12,13,14,15]]])

print("A=",A)
print("B=",B)

# Accessing specific elements using indexing
# A[row, column] -> Selecting row 3, column 3
# B[depth, row, column] -> Selecting depth=1, row=0, column=3
print("A(3,3) =", A[3,3])
print("B(1,0,3) =", B[1,0,3])

# Printing a specific row
# A[row, :] selects all columns from a given row
# B[depth, row, :] selects all columns from a given row in a specific matrix
print("A: Row 1:", A[1,:])
print("B: Row 1:", B[0,1,:])

# Printing a specific column
# A[:, column] selects all rows from a given column
# B[depth, :, column] selects all rows from a given column in a specific matrix
print("A: Column 2:", A[:,2])
print("B: Column 2:", B[0,:,2])

# Printing from first item to sixth with step 2 in row 0
print(A[0, 0:6:2])

# Printing the minimum and the maximum of the matrix A
print("Minimum of A:", np.min(A))
print("Maximum of A:", np.max(A))

# Printing the sum of all items in matrix A
print("Sum:", np.sum(A))
