from matplotlib import pyplot as plt

# X-axis values
Values_X = [1, 2, 3, 4, 5]

# Y-axis values
Values_Y1 = [1, 2, 3, 4, 3]
Values_Y2 = [8, 6, 7, 8, 7]
Values_Y3 = [7, 8, 6, 7, 8]

# Creating the stack plot
plt.stackplot(Values_X, Values_Y1, Values_Y2, Values_Y3, labels=['Values 1','Values 2','Values 3'])

# Adding legend
plt.legend(loc='upper left')

# Adding a title to the graph
plt.title('Stack plot')

# Preventing the overlapping of labels or elements
plt.tight_layout()

# Displaying the plot window
plt.show()
