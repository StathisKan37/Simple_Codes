import cv2
import numpy as np

# Reading and showing the demo image 
img = cv2.imread('demo_image.png', cv2.IMREAD_COLOR)
cv2.imshow('Demo image', img)

# Getting the height and width of the image
img_height = img.shape[0]
img_width = img.shape[1]

# The translation matrix
trans_mat = np.array([[1, 0, 100],[0, 1, 100]], dtype=np.float32)

# Applying and showing the translation
img_trans = cv2.warpAffine(src=img, M=trans_mat, dsize=(img_width, img_height))
cv2.imshow('Translated image', img_trans)

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
