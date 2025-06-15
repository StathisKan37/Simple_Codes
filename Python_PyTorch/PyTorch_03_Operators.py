import torch

# Initializing two tensors
tensor_A = torch.tensor([[ 1, 2, 3, 4],[ 5, 6, 7, 8]])
print('Tensor A:\n', tensor_A)
tensor_B = torch.tensor([[ 9,10,11,12],[13,14,15,16]])
print('Tensor B:\n', tensor_B)

# Tensor addition
tensor_add = torch.add(tensor_B, tensor_A)
print('Tensor B + A:\n', tensor_add)

# Tensor substraction
tensor_sub = torch.sub(tensor_B, tensor_A)
print('Tensor B - A:\n', tensor_sub)

# Tensor multiplication
tensor_mul = torch.mul(tensor_B, tensor_A)
print('Tensor B * A:\n', tensor_mul)

# Tensor division
tensor_div = torch.div(tensor_B, tensor_A)
print('Tensor B / A:\n', tensor_div)

# Tensor modulus remainder
tensor_mod = torch.remainder(tensor_B, tensor_A)
print('Tensor B % A:\n', tensor_mod)

# Tensor powers
tensor_pow = torch.pow(tensor_B, tensor_A)
print('Tensor B ^ A:\n', tensor_pow)

# Tensor C is the transpose of tensor A
tensor_C = tensor_A.T
print('Tensor C:\n', tensor_C)

# Matrix multiplication
tensor_mmul = tensor_A @ tensor_C
print('Matrix multiplication:\n', tensor_mmul)
