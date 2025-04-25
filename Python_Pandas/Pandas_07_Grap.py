import pandas as pd

# Importing the csv file 'Datas_1_Cars.csv'
dataframe = pd.read_csv('Datas_Cars.csv')
print('Data Frame:')
print(dataframe)
print('----------------------------------------------')

# Grapping the first 3 rows
print('3 FIRST ROWS:\n')
print(dataframe.head(3))
print('----------------------------------------------')

# Grapping the last 3 rows
print('3 LAST ROWS:\n')
print(dataframe.tail(3))
print('----------------------------------------------')

# Grabbing a specific row
print('3RD ROW:\n')
print(dataframe.loc[2])
print('----------------------------------------------')

# Grabbing a specific point
print('2ND CAR MODEL:\n')
print(dataframe.loc[1,'Model'])
print('----------------------------------------------')

# Grabbing a subset
print('ENGINE SIZE OF SPECIFIC CARS:\n')
print(dataframe.loc[[0,1,4,13], ['Model', 'Brand', 'Engine Size']])
print('----------------------------------------------')
