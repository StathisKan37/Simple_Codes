import pandas as pd

# Importing the csv file 'Datas_Cars.csv'
dataframe = pd.read_csv('Datas_Cars.csv')

# Creating a function
# Liters -> Cubic Centimeters
def cc_size(x):
	return str(x*1000) + 'cc'

# Applying the function
dataframe['Engine Size'] = dataframe['Engine Size'].apply(cc_size)

# Printing the result
print('ENGINE SIZE IN CC:')
print(dataframe)
print('----------------------------------------------')
