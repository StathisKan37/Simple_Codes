import cv2 as cv

# Reading an 500x500 png image and saving it in the variable 'img'
img=cv.imread('demo_image.png')

# Showing the image in the normal size
cv.imshow('500x500 image', img)

# Scaling the image and shwoing the result
# 250x250
img_1 = cv.resize(img, (250,250), interpolation=cv.INTER_AREA)
cv.imshow('250x250 resized', img_1)
# 750x750
img_2 = cv.resize(img, (750,750), interpolation=cv.INTER_AREA)
cv.imshow('750x750 resized', img_2)

# Waiting for key 0 to continue
cv.waitKey(0)
