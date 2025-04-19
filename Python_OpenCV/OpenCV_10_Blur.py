import cv2 as cv

# Blur methods:

# Loading and showing the demo image
img = cv.imread('demo_image.png')
cv.imshow('Demo image', img)

# Average blur
img_av = cv.blur(img, (7,7))
cv.imshow('Average blur', img_av)

# Gaussian blur
img_gaus = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian blur', img_gaus)

# Median blur
img_med = cv.medianBlur(img, 7)
cv.imshow('Median blur', img_med)

# Bilateral blur
img_bil = cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('Bilateral blur', img_bil)

cv.waitKey(0)
