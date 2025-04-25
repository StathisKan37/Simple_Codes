import pandas as pd

# Importing the csv file 'Datas_Characters.csv'
dataframe = pd.read_csv('Datas_Cars.csv')
print('Data Frame:')
print(dataframe)
print('----------------------------------------------')

# Grouping cars by Cylinders
group_1 = dataframe.groupby('Cylinders')

# Number of cars in each group
print('NUMBER OF CARS OF EACH GROUP:\n')
print(group_1.count())

# Average horsepower
print('AVERAGE HORSEPOWER:\n')
print(group_1['Horsepower'].mean())
print('----------------------------------------------')

# Minimum horsepower
print('MINIMUM HORSEPOWER:\n')
print(group_1['Horsepower'].min())
print('----------------------------------------------')

# Maximum horsepower
print('MAXIMUM HORSEPOWER:\n')
print(group_1['Horsepower'].max())
print('----------------------------------------------')

# Describing each group
print('DESCRIPTION OF EACH GROUP:\n')
print(group_1.describe())
print('----------------------------------------------')
