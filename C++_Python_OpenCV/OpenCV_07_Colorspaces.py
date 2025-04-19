import cv2

# Reading and showing the demo image 
img = cv2.imread('demo_image.png', cv2.IMREAD_COLOR)
cv2.imshow('BGR colorspace', img)

# BGR to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale colorspace', img_gray)

# BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB colorspace', img_rgb)

# BGR to LAB
img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB colorspace', img_lab)

# BGR to YCrCb
img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('YCrCb colorspace', img_ycrcb)

# BGR to HSV
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV colorspace', img_hsv)

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
