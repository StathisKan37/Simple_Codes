import torch

# A torch.Tensor is a multi-dimensional matrix containing elements of a single data type
# Torch defines tensor types
# They work better on GPUs than Numpy arrays
# Default data type: float32

# Initializing a tensor, directly from data
tensor_1 = torch.tensor([[1, 2],[3, 4]])
print('Tensor:\n', tensor_1)

# Initializing a tensor with zeros
tensor_2 = torch.zeros_like(tensor_1)
print('Tensor with zeros:\n', tensor_2)

# Initializing a tensor with ones, from another tensor
tensor_3 = torch.ones_like(tensor_1)
print('Tensor with ones:\n', tensor_3)

# Initializing a tensor with random floats, from another tensor
tensor_4 = torch.rand_like(tensor_2, dtype=torch.float)
print('Tensor with random floats:\n', tensor_4)

# Initializing a tensor with elements from 0 to 9
tensor_5 = torch.arange(10)
print('Tensor with elements from 0 to 9:\n', tensor_5)

# Tensors with specific shape
tensor_shape = (2,3)

tensor_6 = torch.rand(tensor_shape)
print('2x3 Tensor with random floats:\n', tensor_6)

tensor_7 = torch.ones(tensor_shape)
print('2x3 Tensor with ones:\n', tensor_7)

tensor_8 = torch.zeros(tensor_shape)
print('2x3 Tensor with zeros:\n', tensor_8)

#-----------------
# MORE DATA TYPES
#-----------------
# 32-bit floating point: 'torch.float32' or 'torch.float'
# 64-bit floating point: 'torch.float64' or 'torch.double'
# 16-bit floating point: 'torch.float16' or 'torch.half' or 'torch.bfloat16'
#  32-bit complex: 'torch.complex32' or 'torch.chalf'
#  64-bit complex: 'torch.complex64' or 'torch.cfloat'
# 128-bit complex: 'torch.complex128' or 'torch.cdouble'
#  8-bit integer (unsigned): 'torch.uint8'
# 16-bit integer (unsigned): 'torch.uint16'
# 32-bit integer (unsigned): 'torch.uint32'
# 64-bit integer (unsigned): 'torch.uint64'
#    8-bit integer (signed): 'torch.int8'
#   16-bit integer (signed): 'torch.int16' or 'torch.short'
#   32-bit integer (signed): 'torch.int32' or 'torch.int'
#   64-bit integer (signed): 'torch.int64' or 'torch.long'
# Boolean: 'torch.bool'
# Quantized 8-bit integer (unsigned): 'torch.quint8'
#   Quantized 8-bit integer (signed): 'torch.qint8'
#  Quantized 32-bit integer (signed): 'torch.qint32'
# Quantized 4-bit integer (unsigned): 'torch.quint4x2'
# 8-bit floating point, e4m3: 'torch.float8_e4m3fn'
# 8-bit floating point, e5m2: 'torch.float8_e5m2'

# DATATYPES SOURCE:
# https://pytorch.org/docs/stable/tensors.html
