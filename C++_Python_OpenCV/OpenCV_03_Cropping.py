import cv2

# Reading and showing the demo image 
img = cv2.imread('demo_image.png', cv2.IMREAD_COLOR)
cv2.imshow('Demo image', img)
 
# Cropping the image and saving it in the variable 'img_crop'
img_crop = img[65:430, 10:375]
 
# Display the cropped image
cv2.imshow("Cropped image", img_crop)

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
