import cv2 as cv

# Loading the demo image
img = cv.imread('demo_image.png')

# Spliting the color channels of the demo image
# img_B: Blue channel
# img_G: Green channel
# img_R: Red channel
img_B, img_G, img_R = cv.split(img)

# Showing the color channels
cv.imshow('Blue channel', img_B)
cv.imshow('Green channel', img_G)
cv.imshow('Red channel', img_R)

img_bgr = cv.merge([img_B, img_G, img_R])
cv.imshow('BGR image', img_bgr)

cv.waitKey(0)
