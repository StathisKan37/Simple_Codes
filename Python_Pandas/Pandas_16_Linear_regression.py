import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

# Loading the diabets dataset
diabetes = load_diabetes()

# Converting the data to pandas fdataframe
dataframe = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

# Adding the target (24-346)
dataframe['target'] = diabetes.target

print(dataframe)

# Splitting data to X and Y
X = dataframe.drop('target', axis=1)
Y = dataframe['target']
print(X.shape, Y.shape)

# Splitting data to trainning and testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Displaying the shape of training and testing sets
print('Training set shape', X_train.shape, Y_train.shape)
print('Testing set shape', X_test.shape, Y_test.shape)

# Creating and training the Linear Regression model
lr = LinearRegression()
lr.fit(X_train, Y_train)

# Training the model on the training set
lr.fit(X_train, Y_train)

# Predicting on the testing
# Y_pred are predicted values of the target variable based on the features
# Once we have those predictions, we can compare rthem to the actual values the target variable
# To evaluate the performance of the model
Y_pred = lr.predict(X_test)

# Evaluate the performance of the model
print('R2 score: ', r2_score(Y_test, Y_pred))
print('Mean squared error: ', mean_squared_error(Y_test, Y_pred))
print('Mean Absolute error: ', mean_absolute_error(Y_test, Y_pred))
print('intercept: ', lr.intercept_)

# r2_score():
# Variance of the dependent variable (target) explained by theindependent variables (features)
# How well the model fits the data
# Higher is better

# mean_squared_error():
# Average square distance between the predicted and the actual values
# Lower is better

# mean_absolute_error():
# Average absolute distance between the predicted and actual values
# Lower is better

# lr.intercept_:
# Starting point of the regression on the y-axis
# Value of the dependent value (target) when the independent variables (features) are zero
# If positive number , targetincreases as features increase

# Plot predicted vs actual values
# Predicted values of the target variable are plotted on the x-axis
# Actual values of the target variable are plotted on the y-axis
# If the model is good fit, the points should be close to the diagonal line,
# indicating a strong linear relationship between the actual and the predicted values
plt.scatter(Y_test, Y_pred, alpha=0.5)
plt.plot([Y.min(), Y.max()], [Y.min(), Y.max()], color='red')
plt.xlabel('Actual valiues')
plt.ylabel('Predicted values')
plt.title('Predicted vs Actual values (Linear Regression)')
plt.show()

# Plot the residuals
# The residuals are plotted against the predicted values of the target variable.
# If the linear regression model is a good fit for the data,
# the residual plot should show a random scatter of the points around zero
# with no discernable trend.
plt.scatter(Y_pred, Y_test - Y_pred, alpha=0.5)
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot (Linear Regression)")
plt.show()
