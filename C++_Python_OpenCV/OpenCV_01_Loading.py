# Importing the cv2 library as cv
import cv2

# Printing the version of OpenCV
print("OpenCV version:", cv2.__version__)

# Reading the demo image and saving it in the variable 'img'
img = cv2.imread('demo_image.png',cv2.IMREAD_COLOR)

# Reading the demo image in grayscale and saving it
img_gray = cv2.imread('demo_image.png',cv2.IMREAD_GRAYSCALE)

# Alternatively:
# IMREAD_COLOR: 1
# IMREAD_GRAYSCALE: 0
# IMREAD_UNCHANGED: -1

# Displaying the images inside a window
cv2.imshow('Demo image',img)  
cv2.imshow('Grayscale image',img_gray)
 
# Waiting for a keystroke
cv2.waitKey(0)  
 
# Destroying all the windows created
cv2.destroyAllWindows()
