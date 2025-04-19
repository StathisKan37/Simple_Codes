import cv2 as cv
import numpy as np
# Bitwise functions:

# A 400x400 matrix with zeros
blank = np.zeros((400,400), dtype='uint8')

# A black image with a white rectangle
# Top-left: (x=40, y=40)
# Buttom-right: (x=360, y=360)
# Color: 255 (white)
# Thickness: -1 (filled)
img_1 = cv.rectangle(blank.copy(), (40,40), (360,360), 255, -1)
cv.imshow('Image1', img_1)

# A black image with a white circle
# Center: (x=200, y=200)
# Radious: 190
# Color: 255 (white)
# Thickness: -1 (filled)
img_2 = cv.circle(blank.copy(), (200,200), 190, 255, -1)
cv.imshow('Image2', img_2)

# Bitwise AND
img_AND = cv.bitwise_and(img_1, img_2)
cv.imshow('Image1 AND Image2', img_AND)

# Bitwise OR
img_OR = cv.bitwise_or(img_1, img_2)
cv.imshow('Image1 OR Image2', img_OR)

# Bitwise XOR
img_XOR = cv.bitwise_xor(img_1, img_2)
cv.imshow('Image1 XOR Image2', img_XOR)

# Bitwise NOT
img_NOT = cv.bitwise_not(img_1)
cv.imshow('NOT Image1', img_NOT)

cv.waitKey(0)
