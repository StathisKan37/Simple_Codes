import cv2 as cv
import numpy as np
# Masking:

# Loading and showing the demo image
img = cv.imread('demo_image.png')
cv.imshow('Demo image', img)

# A 500x500 matrix with zeros
blank = np.zeros((500,500), dtype='uint8')

# A circle mask
masking = cv.circle(blank.copy(), (190,250), 180, 255, -1)
cv.imshow('Mask', masking)

# Maskink the demo image
img_mask = cv.bitwise_and(img, img, mask=masking)
cv.imshow('Masked image', img_mask)

cv.waitKey(0)
