import cv2

# Reading and showing the demo image 
img = cv2.imread('demo_image.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale demo image', img)

# Thresh: 127
# Max Value: 255

# Binary Threshold
th, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary threshold (thresh:127, max:255)', img_bin)

# Inverse Binary Threshold
th, img_inv_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Inverse binary threshold (thresh:127, max:255)', img_inv_bin)

# Truncate Threshold
th, img_trun = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow('Truncate threshold (thresh:127, max:255)', img_trun)

# Threshold to zero
th, img_zero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow('Threshold to zero (thresh:127, max:255)', img_zero)

# Inverted Threshold to zero
th, img_inv_zero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow('Inverted threshold to zero (thresh:127, max:255)', img_inv_zero)

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
