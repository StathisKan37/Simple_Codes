from matplotlib import pyplot as plt

# Pie chart
# Value_1: Value: 60, Color: Blue
# Value_2: Value: 30, Color: Orange
# Value_3: Value: 10, Color: Green
plt.pie([60, 30, 10], labels=['Value_1', 'Value_2', 'Value_3'], colors=['blue', 'orange', 'green'])

# Adding a title to the graph
plt.title('Pie chart')

# Preventing the overlapping of labels or elements
plt.tight_layout()

# Displaying the plot window
plt.show()
