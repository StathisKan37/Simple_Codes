from matplotlib import pyplot as plt

# Sample data
Values_X = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
Values_Y = [3, 10, 22, 28, 35, 45, 52, 58, 70, 85]

# Create the scatter plot
# Marker shape: circle
# Color: Blue
# Points size: 75
# Edges color: Black
# Line width: 1.2
plt.scatter(Values_X, Values_Y, marker='o', color='blue', s=75, edgecolor='black', linewidth=1.2)

# Adding a title to the graph
plt.title('Scatter plot')

# Preventing the overlapping of labels or elements
plt.tight_layout()

# Displaying the plot window
plt.show()

# Other marker shapes:
# 'o' (circle)
# '^' (Upward triangle)
# 'v' (Downward triangle)
# '<' (Left triangle)
# '>' (Right triangle)
# 's' (Square)
# 'D' (Diamond)
# 'd' (Thin diamond)
# '*' (Star)
# '+' (Plus)
# 'x' (X)
# '_' (Horizontal line)
# 'p' (Pentagon)
# 'h' (Hexagon 1)
# 'H' (Hexagon 2)
