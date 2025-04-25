import pandas as pd

# Importing the csv file 'Datas_Characters.csv'
dataframe = pd.read_csv('Datas_Cars.csv')
print('Data Frame:')

# Creating a new column
dataframe['Car Index'] = [
'Car 1','Car 2','Car 3','Car 4',
'Car 5','Car 6','Car 7','Car 8',
'Car 9','Car 10','Car 11','Car 12',
'Car 13','Car 14','Car 15','Car 16']
print(dataframe)
print('----------------------------------------------')

# Setting Index
dataframe.set_index('Car Index', inplace=True)
print('INDEX SETTED:\n')
print(dataframe)
print('----------------------------------------------')

# Resetting Index
dataframe.reset_index(inplace=True)
print('INDEX RESETTED:\n')
print(dataframe)
print('----------------------------------------------')

# To drop 'Car Index' column:
# dataframe.drop('Car Index', axis=1, inplace=True)
