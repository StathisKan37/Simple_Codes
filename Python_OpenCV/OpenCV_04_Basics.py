import cv2 as cv
# Some basic and useful OpenCV functions:

# Loading and showing the demo image
img = cv.imread('demo_image.png')
cv.imshow('Demo image', img)

# Converting the demo image to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale color', img_gray)

# Converting the demo image blured
img_blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur image', img_blur)

# Edge cascade
img_canny = cv.Canny(img, 125, 175)
cv.imshow('Image edges', img_canny)

# Dilating the image
img_dilate = cv.dilate(img_canny, (7,7), iterations=1)
cv.imshow('Dilated image', img_dilate)

# Eroding the image
img_erode = cv.erode(img_dilate, (3,3), iterations=1)
cv.imshow('Eroded image', img_erode)

cv.waitKey(0)
