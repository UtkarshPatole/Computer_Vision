import os
import cv2
print(cv2.__version__)



img_path = cv2.imread(os.path.join(".", 'Owl.jpg'))

img = img_path

cv2.imshow("Image", img)
cv2.waitKey(0)

video_path = os.path.join(".", 'Video.mp4')

video = cv2.VideoCapture(video_path)

ret = True
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow("Video", frame)
        cv2.waitKey(25)

video.release()
cv2.destroyAllWindows()

# Read Webcam

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()