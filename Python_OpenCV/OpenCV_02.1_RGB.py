import cv2 as cv

# Loading and showing the demo image
img=cv.imread('demo_image.png')
cv.imshow('Normal color', img)

# Copying the image to three matrixes
img_blue = img.copy()
img_green = img.copy()
img_red = img.copy()

# Saving the dimensions of the image
height = img.shape[0]
width = img.shape[1]

for i in range(height):
	for j in range (width):
		# Deliting the green and red RGBs
		img_blue[i,j,1] = 0
		img_blue[i,j,2] = 0

		# Deliting the blue and red RGBs		
		img_green[i,j,0] = 0
		img_green[i,j,2] = 0

		# Deliting the blue and green RGBs
		img_red[i,j,0] = 0
		img_red[i,j,1] = 0

# Showing the RGB images
cv.imshow('Blue image', img_blue)
cv.imshow('Green image', img_green)
cv.imshow('Red image', img_red)

# Waiting
cv.waitKey(0)
