import cv2 
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel)
path = "C:\\Users\\lakshmanan\\OneDrive\\Pictures\\Camera Roll\\talking-to-the-moon-ym-1920x1080.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
