import pandas as pd
from matplotlib import pyplot as plt

# Importing the csv file 'Datas_Characters.csv'
dataframe = pd.read_csv('Datas_Cars.csv')
print('Data Frame:')
print(dataframe)
print('----------------------------------------------')

# Creating a simple histogram with Cylinders number
# Bins: 4
plt.hist(dataframe['Cylinders'], bins=4)

# Adding a title to the graph
plt.title('Cylinders Histogram')

# Displaying the Histogram window
plt.show()
