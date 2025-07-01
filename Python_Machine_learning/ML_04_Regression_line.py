import matplotlib.pyplot as plt
import numpy
from scipy import stats

# This function returns the regression line
def regress_line(X_array):
  return X_array * slope + intercept

# Two arrays to represent X axis and Y axis
X_array = numpy.sort(numpy.random.randint(0, 99, 30)) - numpy.random.randint(0,10,30)
y_array = numpy.sort(numpy.random.randint(0, 99, 30))

# Linear Regression Calculation
slope, intercept, r, pvalue, std_err = stats.linregress(X_array, y_array)
#     slope: How much y increases for a unit increase in x
# intercept: The value of y when x = 0
#         r: How strong and linear the relationship is (-1 to 1)
#    pvalue: Tests the null hypothesis that the slope is zero
#   std_err: The standard error of the estimated slope.

# Creating the regression line
model_line = list(map(regress_line, X_array))

# Displaying the result
plt.scatter(X_array, y_array)
plt.plot(model_line, X_array)
plt.show()

# SOURCE:
# https://www.w3schools.com/python/python_ml_linear_regression.asp
