import cv2 as cv

# Loading the demo image
img=cv.imread('demo_image.png')

# Adding a rectabgle in the demo image
# Top-left position: (x=8, y=62)
# Botton-right position: (x=372, y=430)
# RGB color: 0, 255, 0 (green)
cv.rectangle(img, (8, 62), (372, 430), (0,255,0), thickness=2)

# Adding an 50x50 filled red square
cv.rectangle(img, (10,440), (60,490), (0,0,255), thickness=cv.FILLED)

# Adding a 25 radious blue circle
cv.circle(img, (90,465), 25, (255,0,0), thickness=cv.FILLED)

# Adding a magenta line
cv.line(img, (120,465), (370,465), (255,0,255), thickness=3)

# Adding a text in the demo image
# Text: 'Sym Jet 14'
# Position: (x=20,y=40)
# Font: Hershey triplex
# Size: 1.5
# Color: 0,255,255 (yellow)
# Thickness: 3
cv.putText(img, 'Sym Jet 14', (20,40), cv.FONT_HERSHEY_TRIPLEX, 1.5, (0,255,255), 3)

# Showing the image
cv.imshow('Demo image', img)

cv.waitKey(0)
