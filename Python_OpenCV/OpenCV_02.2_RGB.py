import cv2 as cv

# Loading and showing the demo image
img=cv.imread('demo_image.png')
cv.imshow('Normal color', img)

# Copying the image to three matrixes
img_yellow = img.copy()
img_magenta = img.copy()
img_cyan = img.copy()

# Saving the dimensions of the image
height = img.shape[0]
width = img.shape[1]

for i in range(height):
	for j in range (width):
		# Deleting the blue channel
		img_yellow[i,j,0] = 0

		# Deleting the green channel		
		img_magenta[i,j,1] = 0

		# Deleting the red channet
		img_cyan[i,j,2] = 0

# Showing the RGB images
cv.imshow('Yellow image', img_yellow)
cv.imshow('Magenta image', img_magenta)
cv.imshow('Cyan image', img_cyan)

# Waiting
cv.waitKey(0)
