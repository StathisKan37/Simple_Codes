import cv2 as cv

# Loading and showing the demo image
img = cv.imread('demo_image.png')
cv.imshow('Demo image', img)

# Converting the demo image in grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple thresholding
threshold, img_thresh = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
cv.imshow('Simple thresholding', img_thresh)

# Simple inverse thresholding
threshold, img_thresh_inv = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple inverse thresholding', img_thresh_inv)

# Adaptive thresholding
img_adap = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding', img_adap)

cv.waitKey(0)
