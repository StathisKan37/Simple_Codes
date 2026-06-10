import pygame

# Initializing all Pygame modules
pygame.init()

# Creating a window of size 800x500
screen_1 = pygame.display.set_mode((800,500))
# Setting the window title
pygame.display.set_caption('PyGame_02_Moving_dot')
# A clock to manage the frame rate
clock = pygame.time.Clock()
# The running flag setted to TRUE
running = True

# Delta time variable (time between frames)
dt = 0
# Create a vector for the player's position
player_pos = pygame.Vector2(screen_1.get_width() / 2, screen_1.get_height() / 2)

# Main game loop
while running:
	# Exiting the game when the window closes
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	
	# A blue circle in silver background
	screen_1.fill('silver')
	pygame.draw.circle(screen_1, 'blue', player_pos, 40)
	
	# Handling player movement using arrow keys
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		player_pos.y -= 300 * dt
	if keys[pygame.K_DOWN]:
		player_pos.y += 300 * dt
	if keys[pygame.K_LEFT]:
		player_pos.x -= 300 * dt
	if keys[pygame.K_RIGHT]:
		player_pos.x += 300 * dt
	
	# Updating the screen
	pygame.display.flip()
	# Converting milliseconds to seconds
	dt = clock.tick(60) / 1000
	
pygame.quit()
