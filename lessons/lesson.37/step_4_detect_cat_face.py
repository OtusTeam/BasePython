import os
import cv2

cascade_name = "haarcascade_frontalcatface_extended.xml"

CASCADE_PATH = os.path.join(cv2.data.haarcascades, cascade_name)

detector = cv2.CascadeClassifier(CASCADE_PATH)

print(detector)

# file_name = "data/img-cat.jpeg"
file_name = "data/amy-baugess-MNju0A6EeE0-unsplash.jpg"
image = cv2.imread(file_name)
image_h, image_w, _ = image.shape

scale = 0.3

target_d = int(image_w * 0.5), int(image_h * 0.5)

image_small = cv2.resize(image, target_d)

cat_faces = detector.detectMultiScale(image_small)
print(cat_faces)
print(type(cat_faces))
# print(cat_faces.shape)
# print(cat_faces.size)

print("found", len(cat_faces), "cat faces")

for x, y, w, h in cat_faces:
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    color = (150, 200, 100)
    thickness = 2
    cv2.rectangle(image_small, pt1, pt2, color, thickness)

cv2.imshow("Cats", image_small)
cv2.waitKey(0)

