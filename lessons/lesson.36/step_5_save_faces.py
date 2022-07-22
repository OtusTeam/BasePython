import os
import cv2
import random

FRONTALFACE_CASCADE = "haarcascade_frontalface_default.xml"
# FRONTALFACE_CASCADE = "haarcascade_frontalface_alt_tree.xml"


# print("cv2.data.haarcascades", cv2.data.haarcascades)
detector = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades,
                                              FRONTALFACE_CASCADE))

print(detector)

f_name = 'data/image-sm.jpg'
image = cv2.imread(f_name)

faces: cv2.Mat = detector.detectMultiScale(image)
print(faces)
print(type(faces))
print(faces.shape)
print(faces.size)

print("found", len(faces), "faces")
for x, y, w, h in faces:
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    color = (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255),
    )
    thickness = 2
    cv2.rectangle(image, pt1, pt2, color, thickness)

# cv2.imshow("image with faces", image)
# cv2.waitKey(0)
cv2.imwrite("data/image-sm_faces.jpg", image)

