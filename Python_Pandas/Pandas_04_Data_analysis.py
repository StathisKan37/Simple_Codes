import pandas as pd

# Importing the csv file 'Datas_1_Cars.csv'
dataframe = pd.read_csv('Datas_Cars.csv')
print('Data Frame:')
print(dataframe)
print('----------------------------------------------')

# Counting distinct values (Descending)
print('Number of cars by year:\n')
print(dataframe['Release Year'].value_counts())
# For Ascending short:
# dataframe['Release Year'].value_counts(ascending=True)
print('----------------------------------------------')

# Counting distinct values in percentage
print('Percentage of cars by year:\n')
print(dataframe['Release Year'].value_counts(normalize = True))
print('----------------------------------------------')

# Get specific item count
print('2022 cars:', dataframe['Release Year'].value_counts()[2022])
print('----------------------------------------------')

# Grouping by size
print('Grouped by size:\n')
print(dataframe.groupby('Release Year').size())
print('----------------------------------------------')

# Grouping by count
print('Grouped by count:\n')
print(dataframe.groupby('Release Year').count())
