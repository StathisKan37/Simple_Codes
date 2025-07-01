import numpy
import matplotlib.pyplot as plt

# An array with 2500 random floats from 0 to 1
test_array = numpy.random.normal(0, 1, 2500)

# Histogram with 100 bars of the array
plt.hist(test_array, 100)
plt.show()

# SOURCE:
# https://www.w3schools.com/python/python_ml_normal_data_distribution.asp
