import os
import random

import cv2

CASCADE = 'haarcascade_frontalface_default.xml'

face_finder = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades,
                                                 CASCADE))

f_name = 'data/image-sm.jpg'
image = cv2.imread(f_name)

faces = face_finder.detectMultiScale(image)
for x, y, w, h in faces:
    pt_1 = (x, y)
    pt_2 = (x + w, y + h)
    color = (random.randint(0, 255),
             random.randint(0, 255),
             random.randint(0, 255))
    thickness = 2
    cv2.rectangle(image, pt_1, pt_2, color, thickness)


cv2.imwrite('data/image-sm_faces.jpg', image)

