import torch

# Initializing a tensor with elements from 0 to 12
tensor_1 = torch.arange(12)
print('Tensor:\n', tensor_1)

# Reshaping the tensor to 3x4
tensor_2 = tensor_1.reshape(3,4)
print('Tensor reshaped\n:', tensor_2)

# Reshaping with unknown number of rows
tensor_3 = tensor_1.reshape(-1,4)
print('Tensor reshaped\n:', tensor_3)

# Reshaping with unknown number of columns
tensor_4 = tensor_1.reshape(3,-1)
print('Tensor reshaped\n:', tensor_4)

# 'view' is similar to 'reshape'
tensor_5 = tensor_1.view(3,4)
print('Tensor reshaped\n:', tensor_5)

# If any element from tensor 1 changes,
# it will also change in reshaped tensors
