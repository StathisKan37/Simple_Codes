import pandas as pd

# Importing the csv file 'Datas_1_Cars.csv'
dataframe = pd.read_csv('Datas_Cars.csv')

# Removing the 4rth column (Cylinders)
dataframe.drop('Cylinders', axis=1, inplace=True)

# Removing the fifth row (BMW 330i)
dataframe.drop(4, axis=0, inplace=True)

print('Data Frame:')
print(dataframe)
