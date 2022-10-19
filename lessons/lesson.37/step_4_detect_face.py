import os
from random import randint
import cv2

cascade_name = "haarcascade_frontalface_default.xml"
# cascade_name = "haarcascade_smile.xml"

CASCADE_PATH = os.path.join(cv2.data.haarcascades, cascade_name)

detector = cv2.CascadeClassifier(CASCADE_PATH)

print(detector)

# file_name = "data/img-cat.jpeg"
file_name = "data/image-sm.jpg"
# file_name = "data/image-sm.jpg"
image = cv2.imread(file_name)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = detector.detectMultiScale(image_gray)
print(faces)
print(type(faces))
# print(faces.shape)
# print(faces.size)

print("found", len(faces), "faces")

for x, y, w, h in faces:
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    # color = (150, 200, 100)
    color = (
        randint(0, 255),
        randint(0, 255),
        randint(0, 255),
    )
    thickness = 2
    cv2.rectangle(image, pt1, pt2, color, thickness)

cv2.imshow("Cats", image)
cv2.waitKey(0)

cv2.imwrite("data/img-smile-faces.jpg", image)
