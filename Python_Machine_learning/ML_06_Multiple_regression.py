import pandas
from sklearn import linear_model

# Pandas allows us to read csv files and return a DataFrame
dataframe = pandas.read_csv('car_data.csv')
print(dataframe)

# array_x: The independent values
# array_y: The dependent values
array_x = dataframe[['Weight', 'Volume']]
array_y = dataframe['CO2']

# LinearRegression() creates a linear regression object
reg_line = linear_model.LinearRegression()

# fit() fills the regression object with data that describes the relationship
reg_line.fit(array_x, array_y)

# Predicting the CO2 emission of a test car
print('CO2 prediction:')
print('Car weight: 2300kg')
print('Car volume: 1300cm3')
print(f'CO2 emissions: {reg_line.predict([[2300, 1300]])}')

# SOURCE:
# https://www.w3schools.com/python/python_ml_multiple_regression.asp
