from matplotlib import pyplot as plt

# Sample data for the X and Y axes
dev_x = [1, 6, 10, 15, 19, 24, 31, 35, 49, 56]
dev_y = [49, 55, 59, 65, 69, 74, 81, 85, 89, 96]

# Plotting the data points with a line graph
plt.plot(dev_x, dev_y)

# Labeling X-axis and Y-axis
plt.xlabel('X Values')
plt.ylabel('Y Values')

# Adding a title to the graph
plt.title('My first plot')

# Displaying the plot window
plt.show()
