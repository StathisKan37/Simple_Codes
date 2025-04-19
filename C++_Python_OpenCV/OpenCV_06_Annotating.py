import cv2

# Reading the demo image 
img = cv2.imread('demo_image.png', cv2.IMREAD_COLOR)

# Drawing a LINE
# From (50,50) to (450,450)
# Color: Blue (255,0,0)
# Thickness: 6px
pointA = (50,50)
pointB = (450,450)
cv2.line(img, pointA, pointB, (255, 0, 0), thickness=6)

# Drawing a CIRCLE
# Center: (70,170)
# Radius: 50px
# Color: Green (0,255,0)
# Thickness: 6px
cv2.circle(img, (70,170), 50, (0, 255, 0), thickness=6, lineType=cv2.LINE_AA)

# Drawing a FILLED CIRCLE
# Center: (70,300)
# Radius: 50px
# Color: Red (0,0,255)
cv2.circle(img, (70,300), 50, (0, 0, 255), thickness=-1, lineType=cv2.LINE_AA)

# Drawing a RECTANGLE
# Top-left: (130, 30)
# Buttom-right: (450, 100)
# Color: Magenta (255,0,255)
# Thickness: 6px
cv2.rectangle(img, (130,30), (450, 100), (255,0,255), thickness=6)

# Drawing an ELLIPSE
# Center: (350, 160)
# Axis: (120, 45)
# Angle: 0 degrees
# Perimeter: 0-360 degrees
# Color: Cyan (255,255,0)
# Thickness: 6px
cv2.ellipse(img, (350,160), (120,45), 0, 0, 360, (255, 255, 0), thickness=6)

# Drawing an HALF-ELLIPSE
# Center: (350, 190)
# Axis: (120, 45)
# Angle: 0 degrees
# Perimeter: 0-180 degrees
# Color: Cyan (0,255,255)
# Thickness: 6px
cv2.ellipse(img, (350,190), (120,45), 0, 0, 180, (0, 255, 255), thickness=6)

# TEXT
# Text: 'Hello World!'
# Position: (10,470)
# Font: 3 (FONT_HERSHEY_COMPLEX)
# Scale: 2
# Color: Blue (255,0,0)
# Thickness: 3
cv2.putText(img, 'Hello World!', (10, 470), 3, 2, (255,0,0), 3)

# Alternative Fonts:
# FONT_HERSHEY_SIMPLEX        = 0
# FONT_HERSHEY_PLAIN          = 1
# FONT_HERSHEY_DUPLEX         = 2
# FONT_HERSHEY_COMPLEX        = 3
# FONT_HERSHEY_TRIPLEX        = 4
# FONT_HERSHEY_COMPLEX_SMALL  = 5
# FONT_HERSHEY_SCRIPT_SIMPLEX = 6
# FONT_HERSHEY_SCRIPT_COMPLEX = 7
# FONT_ITALIC                 = 16

# Showing the drawed image
cv2.imshow('Drawed image', img)

# Waiting for key 0 to destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
