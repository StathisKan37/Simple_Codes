import matplotlib.pyplot as plt
import numpy
from sklearn.metrics import r2_score
# Train/Test method measures the accuracy of the model

# Optionaly setting random seed to 2
numpy.random.seed(2)

# Two arrays to represent X axis and Y axis
array_x = numpy.random.normal(3, 1, 100)
array_y = numpy.random.normal(150, 40, 100) / array_x

# Splitting data into train and test
# Training set is a random selection of 80%
train_x = array_x[:80]
train_y = array_y[:80]
# Testing set is the remaining 20%.
test_x = array_x[80:]
test_y = array_y[80:] 

# Making a polynomial model
model_object = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))
# Making the linespace
model_line = numpy.linspace(0, 6, 100)

# Displaying the Original data
plt.scatter(array_x, array_y)
plt.title('Original data')
plt.show()

# Displaying the Training data
print(f'R-Squared value for training data: {r2_score(train_y, model_object(train_x))}')
plt.scatter(train_x, train_y)
plt.plot(model_line, model_object(model_line))
plt.title('Training data')
plt.show()

# Displaying the Testing data
print(f'R-Squared value for testing data: {r2_score(test_y, model_object(test_x))}')
plt.scatter(test_x, test_y)
plt.title('Testing data')
plt.show()

# SOURCE:
# https://www.w3schools.com/python/python_ml_train_test.asp
