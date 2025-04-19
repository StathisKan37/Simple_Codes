import cv2 as cv
# Contour detection:

# Loading and showing the demo image
img = cv.imread('demo_image.png')
cv.imshow('Demo image', img)

# Converting the image to grayscale and blur
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(img_gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Grayscaled image', img_blur)

# Edge cascade
img_canny = cv.Canny(img, 125, 175)
cv.imshow('Image edges', img_canny)

contours, hierarchies = cv.findContours(img_canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print('Contours found:', len(contours))

cv.waitKey(0)
