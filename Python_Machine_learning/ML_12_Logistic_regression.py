import matplotlib.pyplot as plt
import numpy
from sklearn import linear_model 

# X_array: independent variables (features)
# y_array: dependent variables (binary target labels)
X_array = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y_array = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# Creating a logistic regression object
logr = linear_model.LogisticRegression()
logr.fit(X_array,y_array)

# Predicting the y value if X = 3.46
predicted = logr.predict(numpy.array([3.46]).reshape(-1,1))
print(f'For X = 3.46, y = {predicted}') 

# Converting log-odds to odds by exponentiation
log_odds = logr.coef_
odds = numpy.exp(log_odds)
print(f'Odds: {odds}')

# Displaying the result
plt.scatter(X_array, y_array)
plt.show()

# SOURCE:
# https://www.w3schools.com/python/python_ml_logistic_regression.asp
