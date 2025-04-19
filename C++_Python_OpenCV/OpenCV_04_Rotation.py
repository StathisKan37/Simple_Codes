import cv2

# Reading and showing the demo image 
img = cv2.imread('demo_image.png', cv2.IMREAD_COLOR)
cv2.imshow('Demo image', img)

# Image Rotation:
# Angle: 45 degrees
# Calculating the center of the image
img_height = img.shape[0]
img_width = img.shape[1]
img_center = (img_width/2, img_height/2)
# Rotating the matrix by 45 degrees
rotation_matix = cv2.getRotationMatrix2D(img_center, 45, scale=1)
# Rotating the image using cv2.warpAffine
img_rot = cv2.warpAffine(src=img, M=rotation_matix, dsize=(img_width, img_height))
# Showing the rotated image
cv2.imshow('Rotated image', img_rot)

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
