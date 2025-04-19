from matplotlib import pyplot as plt
import numpy as np

# Sample data for the X and Y axes
dev_x1 = np.array([0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800])
dev_y1 = [1200, 1800, 2600, 3600, 4800, 6200, 7800, 9600, 11600, 13800]

dev_x2 = np.array([0, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800])
dev_y2 = [700, 1100, 1700, 2500, 3500, 4700, 6100, 7700, 9500, 11500]

# Displaying the data with a bars
# Offsetting (-25, +25), so the bars will not overlap
# Values 1 in blue bar
plt.bar(dev_x1 - 25, dev_y1, width=50, color='b', label='Values 1')
# Values 2 in red bar
plt.bar(dev_x2 + 25, dev_y2, width=50, color='r', label='Values 2')


# Labeling X-axis and Y-axis
plt.xlabel('X Values')
plt.ylabel('Y Values')

# Adding a title to the graph
plt.title('Bars')

# Displaying the label of each plot
plt.legend()

# Displaying the plot window
plt.show()
