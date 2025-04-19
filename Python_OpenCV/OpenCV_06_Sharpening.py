import cv2 as cv

# Loading and showing the demo image
img=cv.imread('demo_image.png')
cv.imshow('Demo image', img)

# Converting the demo image blured
img_blur = cv.blur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur image', img_blur)

# Subtracting the blured image to the demo
img_edges = cv.subtract(img, img_blur)
img_edges = img_edges * 2
cv.imshow('image details', img_edges)

# Adding the detailed image to the demo image
img_sharp = cv.add(img, img_edges)
# Showing the sharpened image
cv.imshow('Sharpened image', img_sharp)

cv.waitKey(0)
