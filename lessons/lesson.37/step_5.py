import os
from random import random

import cv2

CASCADE = 'haarcascade_frontalface_default.xml'

face_finder = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades,
                                                 CASCADE))

f_path = './data/image-sm.jpeg'
image = cv2.imread(f_path)
im_h, im_w, _ = image.shape

faces = face_finder.detectMultiScale(image)
print(len(faces))
for x, y, w, h in faces:
    # print(x, y, w, h)
    pt_1 = (x, y)
    pt_2 = (x + w, y + h)
    color = (random() * 255, random() * 255, random() * 255)
    thickness = 2
    cv2.rectangle(image, pt_1, pt_2, color, thickness)

cv2.imwrite(f_path.replace('.jpeg', '_faces_fine.jpg'), image)
cv2.imshow('faces on image', image)
key = cv2.waitKey(0)
