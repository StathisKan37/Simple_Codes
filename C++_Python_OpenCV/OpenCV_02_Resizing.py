import cv2

# Reading an 500x500 png image and saving it in the variable 'img'
img=cv2.imread('demo_image.png', cv2.IMREAD_COLOR)

# Showing the image in the normal size
cv2.imshow('500x500 image', img)

# Scaling the image and shwoing the result
# 250x250
img_1 = cv2.resize(img, (250,250), interpolation=cv2.INTER_AREA)
cv2.imshow('250x250 resized', img_1)
# 750x750
img_2 = cv2.resize(img, (750,750), interpolation=cv2.INTER_AREA)
cv2.imshow('750x750 resized', img_2)

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows() 
