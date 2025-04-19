import cv2 as cv
import numpy as np

# Loading and showing the demo image
img = cv.imread('demo_image.png')
cv.imshow('Demo image', img)

# Converting and showing the demo image in grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale image', img_gray)

# Laplacian
img_lap = cv.Laplacian(img_gray, cv.CV_64F)
img_lap = np.uint8(np.absolute(img_lap))
cv.imshow('Laplacian image', img_lap)

# Sobel
img_sobelx = cv.Sobel(img_gray, cv.CV_64F, 1, 0)
img_sobely = cv.Sobel(img_gray, cv.CV_64F, 0, 1)
cv.imshow('X Sobel', img_sobelx)
cv.imshow('Y Sobel', img_sobely)

# Combining the 2 sobel images
img_sobel = cv.bitwise_or(img_sobelx, img_sobely)
cv.imshow('Sobel image', img_sobel)

cv.waitKey(0)
