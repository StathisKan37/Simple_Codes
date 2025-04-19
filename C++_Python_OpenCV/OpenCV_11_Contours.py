import cv2

# Reading and showing the demo image in grayscale
img = cv2.imread('demo_image.png', cv2.IMREAD_COLOR)
cv2.imshow('Demo image', img)

# Converting to Grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Binary Threshold
th, img_thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholded image', img_thresh)

# DETECTING CONTOURS

# CHAIN_APPROX_NONE
contours_1, hierarchy_1 = cv2.findContours(image=img_thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
# Copying the demo image
img_approx_none = img.copy()
# Drawing the contours
# ContourIdx: -1
# Color: Green (0, 255, 0)
# Thickness: 2
cv2.drawContours(image=img_approx_none, contours=contours_1, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow('None approximation', img_approx_none)

# CHAIN_APPROX_SIMPLE
contours_2, hierarchy_2 = cv2.findContours(image=img_thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
# Copying the demo image
img_approx_simple = img.copy()
# Drawing the contours
cv2.drawContours(image=img_approx_simple, contours=contours_2, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow('Simple approximation', img_approx_simple)

# Contour detecting modes
# RETR_TREE
# RETR_LIST
# RETR_EXTERNAL
# RETR_CCOMP

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
