#ColorSpaces

import os
import cv2

img = cv2.imread(os.path.join(".","Bird.jpg"))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", img)
cv2.imshow("RGB Image", img_rgb)
cv2.imshow("Gray Image", img_gray)
cv2.waitKey(0)