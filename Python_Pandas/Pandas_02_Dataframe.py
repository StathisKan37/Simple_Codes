import pandas as pd
import numpy as np

# Creating a dataframe
# Data, Rows and Columns:
dframe_data = np.random.rand(4,3)
dframe_rows = ['Row 1', 'Row 2', 'Row 3', 'Row 4']
dframe_columns = ['Column 1', 'Column 2', 'Column 3']

# Create the dataframe
dataframe_1 = pd.DataFrame(dframe_data, dframe_rows, dframe_columns)
print('Data Frame 1:')
print(dataframe_1)

# Importing the csv file 'Datas_1_Cars.csv'
dataframe_2 = pd.read_csv('Datas_Cars.csv')
print('Data Frame 2:')
print(dataframe_2)
