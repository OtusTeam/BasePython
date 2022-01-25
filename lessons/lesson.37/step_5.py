import os

import cv2

CASCADE = 'haarcascade_frontalface_default.xml'

cascade_path = os.path.join(cv2.data.haarcascades,
                            CASCADE)
face_finder = cv2.CascadeClassifier(cascade_path)

f_path = './data/image-sm.jpg'
img = cv2.imread(f_path)
im_h, im_w, _ = img.shape

faces = face_finder.detectMultiScale(img)
print(len(faces))

for x, y, w, h in faces:
    # print(x, y, w, h)
    pt_1 = (x, y)
    pt_2 = (x + w, y + h)
    color = (127, 127, 127)
    thickness = 2
    cv2.rectangle(img, pt_1, pt_2, color, thickness)

# cv2.imwrite(f_path.replace('.jpeg', '_faces.jpg'), img)
cv2.imshow('faces on image', img)
key = cv2.waitKey(0)
