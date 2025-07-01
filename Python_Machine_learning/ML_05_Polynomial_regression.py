import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Two arrays to represent X axis and Y axis
array_x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
array_y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# Making a polynomial model
model_object = np.poly1d(np.polyfit(array_x, array_y, 3)) 

# Making the linespace
# Starting at position 1, end at position 22
model_line = np.linspace(1, 22, 100)

# Displaying the result
plt.scatter(array_x, array_y)
plt.plot(model_line, model_object(model_line))
plt.show() 

# R Squared: How well the relationship between the values of the x- and y-axis is
# If there are no relationship the polynomial regression can not predict
# The r-squared value ranges from 0 to 1
# 0: No relationship
# 1: 100% related
print(f'R-Squared value: {r2_score(array_y, model_object(array_x))}') 

# Predicting a value
print(f'If x=17, y={model_object(17)}')

# SOURCE:
# https://www.w3schools.com/python/python_ml_polynomial_regression.asp
