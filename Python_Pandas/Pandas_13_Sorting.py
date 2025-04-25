import pandas as pd

# Importing the csv file 'Datas_Cars.csv'
dataframe = pd.read_csv('Datas_Cars.csv')

# Ascending sort
print('ASCENDING SORTED:')
print(dataframe.sort_values('Horsepower', ascending = True))

# Descending sort: 
# dataframe.sort_values('Horsepower', ascending = False)

# For permanently sorting:
# dataframe.sort_values('Horsepower', ascending = True, inplace=True)
# dataframe.sort_values('Horsepower', ascending = False, inplace=True)
