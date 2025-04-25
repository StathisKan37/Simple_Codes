import pandas as pd
from matplotlib import pyplot as plt

# Importing the csv file 'Datas_Characters.csv'
dataframe = pd.read_csv('Datas_Cars.csv')
print('Data Frame:')
print(dataframe)
print('----------------------------------------------')

# Combining Brand and Model into one label
car_labels = dataframe['Brand'] + ' ' + dataframe['Model']

# Creating a simple histogram with Cylinders number
plt.bar(car_labels, dataframe['Horsepower'])

# Adding a title to the graph
plt.title('Horsepower')
# Rotating the x-axis labels by 90 degrees
plt.xticks(rotation=90)
# Adjusting space between plot elements
plt.tight_layout()
# Displaying the Histogram window
plt.show()
