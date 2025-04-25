import pandas as pd
import numpy as np

# Creating a dataframe
dictionary_data = {'A':[1,2,3], 'B':[4,5,6], 'C':[7,8,9]}
dataframe = pd.DataFrame(dictionary_data)
print(dataframe)
print('----------------------------------------------')

# Adding null data
dataframe.iloc[1, 1] = np.nan
print('NULL DATA ADDED:\n')
print(dataframe)
print('----------------------------------------------')

# Dropping the row with null data
print('NULL DATA ROW REMOVED:\n')
print(dataframe.dropna(axis=0))
print('----------------------------------------------')

# Dropping the column with null data
print('NULL DATA COLUMN REMOVED:\n')
print(dataframe.dropna(axis=1))
print('----------------------------------------------')

# Dropping row or column PERMANENTLY:
# dataframe.dropna(axis=0, inplace=True)
# dataframe.dropna(axis=1, inplace=True)

# For more than one null data (3):
# dataframe.dropna(thresh=3, axis=0, inplace=True)
# dataframe.dropna(thresh=3, axis=1, inplace=True)

# Replacing the null data with a value (5)
dataframe.fillna(value=5, inplace=True)
print('NULL DATA REPLACED:\n')
print(dataframe)
