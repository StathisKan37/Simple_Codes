import cv2 as cv

# Loading the demo image
img = cv.imread('demo_image.png')

# BGR to grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale colorspace', img_gray)

# BGR to HSV
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV colorspace', img_hsv)

# BGR to LAB
img_lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB colorspace', img_lab)

# BGR to RGB
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB colorspace', img_rgb)

# HSV to BGR
img_bgr = cv.cvtColor(img_hsv, cv.COLOR_HSV2BGR)
cv.imshow('BGR colorspace', img_bgr)

cv.waitKey(0)
