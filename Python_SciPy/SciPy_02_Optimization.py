from scipy.optimize import root
from scipy.optimize import minimize
from math import cos

# Defining two functions: f1(x) and f2(x)
f1 = lambda x: (x+cos(x))
print('f1(x) = x + cos(x)')
f2 = lambda x: (x**2+x+2)
print('f2(x) = x^2 + x + 2')

# Calculating the root of f1 near the initial guess x=0
f1_root = root(f1, 0)
# Calculating the minimum of f2 starting from x = 0
# BFGS optimization method is used
f2_min = minimize(f2, 0, method='BFGS')

# Printing the results
print(f'Root of f1(x): {f1_root.x}')
print(f'Minimum of f2(x): {f2_min.x}')

# SOURCE:
# https://www.w3schools.com/python/scipy/scipy_optimizers.php
