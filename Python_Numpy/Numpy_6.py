import numpy as np

# Loading the data from the file 'data.txt'
A=np.genfromtxt('data.txt', delimiter=',')
A=A.astype('int16')
print(A)

# Booleam masking
# True: when an item is bigger than 9
# False: when an tiem is less than 9
B = A > 9
print(B)

# True: when an item is bigger than 9 and less than 25
# False: when an tiem is less than 9 or bigger than 25
C = ((A>9)&(A<25))
print(C)
