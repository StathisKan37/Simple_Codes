import cv2

# Reading and showing the demo image in grayscale
img = cv2.imread('demo_image.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale demo image', img)

# Blurring the demo image
img_blur = cv2.GaussianBlur(img,(3,3), 0, 0)
cv2.imshow('Gaussian blurred image', img_blur)

# Sobel Edge Detection on the X axis
img_sobelX = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
cv2.imshow('Sobel X Edge detection', img_sobelX)

# Sobel Edge Detection on the Y axis
img_sobelY = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
cv2.imshow('Sobel Y Edge detection', img_sobelY)

# Sobel Edge Detection on the X and Y axis
img_sobelXY = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
cv2.imshow('Sobel X and Y Edge detection', img_sobelXY)

# Canny Edge Detection
img_canny = cv2.Canny(image=img_blur, threshold1=50, threshold2=150)
cv2.imshow('Canny Edge Detection', img_canny)

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
