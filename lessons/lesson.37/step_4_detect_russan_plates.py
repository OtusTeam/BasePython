import os
from random import randint
import cv2

cascade_name = "haarcascade_russian_plate_number.xml"

CASCADE_PATH = os.path.join(cv2.data.haarcascades, cascade_name)

detector = cv2.CascadeClassifier(CASCADE_PATH)

print(detector)

file_name = "data/car-plates.jpeg"
image = cv2.imread(file_name)
plates = detector.detectMultiScale(image)
print(plates)
print(type(plates))
# print(plates.shape)
# print(plates.size)

print("found", len(plates), "plates")

for x, y, w, h in plates:
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    # color = (150, 200, 100)
    color = (
        randint(50, 255),
        randint(50, 255),
        randint(50, 255),
    )
    thickness = 4
    cv2.rectangle(image, pt1, pt2, color, thickness)

cv2.imshow("Plates", image)
cv2.waitKey(0)

cv2.imwrite("data/img-plates.jpg", image)
