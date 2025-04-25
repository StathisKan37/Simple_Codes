import pandas as pd

# Creating  2 Series in pandas
# Series with integers
list_1 = [1,2,3,4]
series_1 = pd.Series(list_1)
print('Series example 1:')
print(series_1)
# Series with characters
list_2 = ['A', 'B', 'C', 'D']
series_2 = pd.Series(list_2)
print('Series example 2:')
print(series_2)

# Creating Series with dictionary
list_3 = {'Hyundhai':12, 'Toyota':42, 'Mitsubishi': 31}
series_4 = pd.Series(list_3)

# Creating Series with integers and characters
series_3 = pd.Series(list_1, list_2)
print('Series example 4:')
print(series_4)
