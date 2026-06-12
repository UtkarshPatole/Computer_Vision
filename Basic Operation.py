import os

import cv2

image_path = os.path.join(".", 'Dogs.jpg')

img = cv2.imread(image_path)
# resized_img = cv2.resize(img,(130,100))

print(img.shape)
# print(resized_img.shape)

cv2.imshow("Image", img)
# cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)

# Crop Images
cropped_img = img[40:90, 100:200]
cv2.imshow("Cropped Image", cropped_img)   
cv2.waitKey(0)
