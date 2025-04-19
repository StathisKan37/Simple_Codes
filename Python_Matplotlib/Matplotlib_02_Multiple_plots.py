from matplotlib import pyplot as plt

# Hand-drawn XKCD comic style
# plt.xkcd()

# Sample data for the X and Y axes
dev_x1 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
dev_y1 = [1200, 1800, 2600, 3600, 4800, 6200, 7800, 9600, 11600, 13800]

dev_x2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
dev_y2 = [7500, 8800, 9700, 10100, 9900, 9400, 8700, 7900, 7000, 6000]

# Plotting the data points with a line graph
# Values 1 in blue solid line
plt.plot(dev_x1, dev_y1, color='b', linestyle='-', label='Values 1')
# Values 2 in red dashed line with point markers
plt.plot(dev_x2, dev_y2, color='r', linestyle='--', marker='o', label='Values 2')

# Labeling X-axis and Y-axis
plt.xlabel('X Values')
plt.ylabel('Y Values')

# Adding a title to the graph
plt.title('Multiple plots')

# Displaying the label of each plot
plt.legend()

# Saving the figure as .png (figure.png)
# plt.savefig('figure.png')

# Displaying the plot window
plt.show()

# Line Styles
# '-'  (solid line style)
# '--' (dashed line style)
# '-.' (dash-dot line style)
# ':'  (dotted line style)

# Colors
# 'b' (blue)
# 'g' (green)
# 'r' (red)
# 'c' (cyan)
# 'm' (magenta)
# 'y' (yellow)
# 'k' (black)
# 'w' (white)

# Markers
# '.' (point)
# ',' (pixel)
# 'o' (circle)
# 'v' (triangle_down)
# '^' (triangle_up)
# '<' (triangle_left)
# '>' (triangle_right)
# '1' (tri_down)
# '2' (tri_up)
# '3' (tri_left)
# '4' (tri_right)
# '8' (octagon)
# 's' (square)
# 'p' (pentagon)
# 'P' (plus filled)
# '*' (star)
# 'h' (hexagon1)
# 'H' (hexagon2)
# '+' (plus)
# 'x' (X)
# 'X' (X filled)
# 'D' (diamond)
# 'd' (thin_diamond)
# '|' (vline)
# '_' (hline)

# SOURCE:
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
