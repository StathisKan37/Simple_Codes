import pandas as pd

# Importing the csv file 'Datas_1_Cars.csv'
dataframe_1 = pd.read_csv('Datas_Cars.csv')

# Adding a column with default values
# Condition: 'Brand new'
dataframe_1['Condition'] = ['Brand new'] * len(dataframe_1)

# Adding a column in 2nd position
dataframe_1.insert(2, 'Wheel Color', ['Silver'] * len(dataframe_1), True)

# .assign() copys the dataframe to a new dataframe and adds a new column
# Adding a column with default boolean values
# Condition: False
dataframe_2 = dataframe_1.assign(Crashed = [False] * len(dataframe_1))

print('Data Frame:')
print(dataframe_2)
