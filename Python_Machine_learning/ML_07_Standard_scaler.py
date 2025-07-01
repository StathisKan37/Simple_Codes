import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

# Reading the .csv file 'car_data.csv'
dataframe = pandas.read_csv('car_data.csv')
print(dataframe)

# StandardScaler(): returns a Scaler object for transforming data sets
std_scaler = StandardScaler()

# The independent and dependent values
array_x = dataframe[['Weight', 'Volume']]
array_y = dataframe['CO2']

# Fitting the scaler to X and transform it
scaled_x = std_scaler.fit_transform(array_x)

# Creating a linear regression line
reg_line = linear_model.LinearRegression()
reg_line.fit(scaled_x, array_y)

# Predicting the CO2 emission of a test car
print('CO2 prediction:')
print('Car weight: 2300kg')
print('Car volume: 1300cm3')
# Scaling the test input
scaled_test_input = std_scaler.transform([[2300, 1300]])
predicted_co2 = reg_line.predict(scaled_test_input)
print(f'CO2 emissions: {predicted_co2[0]}')

# SOURCE:
# https://www.w3schools.com/python/python_ml_scale.asp
