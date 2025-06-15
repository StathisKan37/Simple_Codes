import torch
import numpy as np

# Initializing a tensor
tensor_torch = torch.tensor([[1,2,3],[4,5,6]])

# Tensor to NumPy matrix
tensor_numpy = tensor_torch.numpy()
print('NumPy matrix:\n', tensor_numpy)

# NumPy matrix to Tensor
tensor_torch = torch.from_numpy(tensor_numpy)
print('PyTorch tensor:\n', tensor_torch)
