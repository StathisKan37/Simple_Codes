import cv2 as cv
import numpy as np
# Some basic and useful OpenCV transformation functions:

# Loading and showing the demo image
img = cv.imread('demo_image.png')
cv.imshow('Demo image', img)

# Saving the dimensions of the image (x=500, y=500)
dimensions=(img.shape[1], img.shape[0])

# Translating the image 150 pixels right and 100 pixels down
# Creating a matrix with floats:
# [ 1, 0, 150 ]
# [ 0, 1, 100 ]
trans_mat = np.float32([[1,0,150],[0,1,100]])
# Translating and showing the image
img_translt=cv.warpAffine(img, trans_mat, dimensions)
cv.imshow('Translated image', img_translt)

# Rotating the image 45 degrees with rotation point (300,250) and scale 1.0
# Saving the rotation point
rot_point = (300,250)
# Creating the rotation matrix
rot_mat = cv.getRotationMatrix2D(rot_point, 45, 1.0)
# Rotating and showing the image
img_rotation = cv.warpAffine(img, rot_mat, dimensions)
cv.imshow('Rotated image', img_rotation)

# Resizing the image
img_resize = cv.resize(img, (300,300), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized image', img_resize)

# Cropping the image
img_crop = img[150:350, 150:350]
cv.imshow('Cropped image', img_crop)

# Flipping the image
#  0: flipping verticaly
#  1: flipping horizonticaly
# -1: flipping verticaly and horizontaly
img_flip = cv.flip(img, 1)
cv.imshow('Flipped image', img_flip)

cv.waitKey(0)
