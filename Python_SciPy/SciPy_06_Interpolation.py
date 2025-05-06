import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf
# Generating points between given points

# x: The domain of the functions
x = np.array([0,1,2,3,4,5,6,7,8,9])
# Defining 2 functions
f1 = 2*x + 1
f2 = x**2 + np.sin(x) + 1
print('f1(x) = 2x + 1')
print('f2(x) = x^2 + sin(x) + 1')

interp_func_1 = interp1d(x, f1)
interp_func_2 = UnivariateSpline(x, f2)
interp_func_3 = Rbf(x, f2)

# Displaying the results
print(f'     1D Interpolation: f1(2.6) = {interp_func_1(2.6)}')
print(f' Spline Interpolation: f2(2.6) = {interp_func_2(2.6)}')
print(f'Radial Basis Function: f2(2.6) = {interp_func_3(2.6)}')

# SOURCE:
# https://www.w3schools.com/python/scipy/scipy_interpolation.php
