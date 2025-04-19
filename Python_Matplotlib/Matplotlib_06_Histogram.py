from matplotlib import pyplot as plt

# Sample data
Values = [55, 67, 72, 80, 62, 85, 90, 76, 66, 74, 88, 82, 59, 77, 81, 68, 73, 79, 84, 75]
bins = [50, 60, 70, 80, 90]

# Creating the histogram
plt.hist(Values, bins=bins, color='blue', edgecolor='white')

# Adding a title to the graph
plt.title('Histogram')

# Preventing the overlapping of labels or elements
plt.tight_layout()

# Displaying the plot window
plt.show()
