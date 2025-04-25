import pandas as pd

# Importing the csv file 'Datas_Characters.csv'
dataframe = pd.read_csv('Datas_Cars.csv')
print('Data Frame:')
print(dataframe)
print('----------------------------------------------')

# Conditional selection
print('ALL BLUE CARS:\n')
print(dataframe[dataframe['Drive Type'] == 'AWD'])
print('----------------------------------------------')

# Conditional selection
print('ALL BRANDS AND MODELS OF RWD CARS:\n')
print(dataframe[dataframe['Drive Type'] == 'RWD'][['Brand', 'Model']])
print('----------------------------------------------')

# Multiple Conditional selection (AND)
print('ALL WHITE 4 CYLINDER CARS:\n')
print(dataframe[(dataframe['Color'] == 'White') & (dataframe['Cylinders'] == 4)])
print('----------------------------------------------')

# Multiple Conditional selection (OR)
print('ALL RED AND ALL BLACK CARS:\n')
print(dataframe[(dataframe['Color'] == 'Red') | (dataframe['Color'] == 'Black')])
print('----------------------------------------------')
