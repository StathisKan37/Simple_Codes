import pygame

# Setting number PI
pi = 3.14159

# Initializing all Pygame modules
pygame.init()

# Creating a window of size 800x500
screen_1 = pygame.display.set_mode((800,500))
# Setting the window title
pygame.display.set_caption('PyGame_01_Shapes_display')
# The running flag setted to TRUE
running = True

# Main game loop
while running:
	# Exiting the game when the window closes
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	# Setting background to silver color
	screen_1.fill('silver')
	
	# Drawing a straight line
	# Surface: screen_1
	# Color: 0,0,255 (Blue)
	# Starting point: (10,10)
	# Ending point: (10,490)
	# Width: 5px
	pygame.draw.line(screen_1, (0,0,255), (10,10), (10,490), width=5)
	
	# Drawing an open polyline
	# Surface: screen_1
	# Color: 0,0,255 (Blue)
	# Closed: False
	# Point 1: (20, 490)
	# Point 2: (20, 10)
	# Point 3: (790, 10)
	# Width: 5px
	pygame.draw.lines(screen_1, (0,0,255), closed=False, points=[(20,490),(20,10),(790,10)], width=5)
	
	# Drawing a closed polyline
	# Surface: screen_1
	# Color: 0,0,255 (Blue)
	# Closed: True
	# Point 1: (550, 70)
	# Point 2: (790, 70)
	# Point 3: (790, 490)
	# Point 4: (650, 490)
	# Point 5: (650, 330)
	# Point 6: (100, 330)
	# Width: 5px
	pygame.draw.lines(screen_1, (0,0,255), closed=True, points=[(550, 70),(790, 70),(790,490),(650,490),(650,330),(100,330)], width=5)
	
	# Drawing an arc
	# Surface: screen_1
	# Color: 0,0,255 (Blue)
	# Ellipse rectangle: (30, 20, 1520, 940)
	# Start angle: 3.14/2
	# Stop angle: 3.14
	# Width: 5px
	pygame.draw.arc(screen_1, (0,0,255), (30,20,1520,940), start_angle=(pi/2), stop_angle=pi, width=5)
	
	# Drawing a rectangle
	# Surface: screen_1
	# Color: 0,0,255 (Blue)
	# Tpo-left: (100, 340)
	# Bottom-right: (100+540, 340+150)
	# Width: 5px
	pygame.draw.rect(screen_1, (0,0,255), (100,340,540,150), width=5)
	
	# Drawing a circle
	# Surface: screen_1
	# Color: 0,0,255 (Blue)
	# Center: (130,120)
	# Radious: 90
	# Width: 5
	pygame.draw.circle(screen_1, (0,0,255), (130,120), 90, width=5)
	
	# Drawing an ellipse
	# Surface: screen_1
	# Color: 0,0,255 (Blue)
	# Ellipse rectangle: (370,140,410,170)
	# Width: 5
	pygame.draw.ellipse(screen_1, (0,0,255), (370,140,410,170), width=5)
	
	# Updating the screen
	pygame.display.flip()

pygame.quit()
