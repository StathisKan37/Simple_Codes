import cv2
import numpy as np

# Reading and showing the demo image 
img = cv2.imread('demo_image.png', cv2.IMREAD_COLOR)
cv2.imshow('Demo image', img)

# Image bluring
img_blur = cv2.blur(src=img, ksize=(5,5))
cv2.imshow('Blured image', img_blur)

# Gaussian image bluring
img_gus = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0, sigmaY=0)
cv2.imshow('Gaussian blured image', img_gus)

# Median bluring
img_med = cv2.medianBlur(src=img, ksize=5)
cv2.imshow('Median blured image', img_med)

# Bilateral filter
img_bil = bilateral_filter = cv2.bilateralFilter(src=img, d=9, sigmaColor=75, sigmaSpace=75)
cv2.imshow('Bilateral filtered image', img_bil)

# Blurring  using Custom 2D-Convolution Kernels
# Kernel 1:
# [ 1, 1, 1, 1, 1]
# [ 1, 1, 1, 1, 1]
# [ 1, 1, 1, 1, 1]
# [ 1, 1, 1, 1, 1]
# [ 1, 1, 1, 1, 1]
kernel_1 = np.ones((5, 5), np.float32) / 25
img_ker_1 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_1)
cv2.imshow('Kernel 1 blur', img_ker_1)

# Kernel 2:
# [  0, -1,  0 ]
# [ -1,  5, -1 ]
# [  0,  1,  0 ]
kernel_2 = np.array([[0, -1,  0],[-1,  5, -1],[0, -1,  0]])
img_ker_2 = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_2)
cv2.imshow('Kernel 2 blur', img_ker_2)

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
