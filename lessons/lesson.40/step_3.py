import os
import random

import cv2

f_name = "data/image-sm.jpg"
# f_name = "data/car-plates.jpeg"
CASCADE = "haarcascade_frontalface_default.xml"
# CASCADE = "haarcascade_license_plate_rus_16stages.xml"

cascade_path = os.path.join(
    cv2.data.haarcascades,
    CASCADE,
)

# print(cascade_path)

def main():
    face_finder = cv2.CascadeClassifier(cascade_path)

    image = cv2.imread(f_name)
    # print(image.shape)
    image_gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY,
    )
    # print(image_gray.shape)
    # print(image_gray)

    faces = face_finder.detectMultiScale(image_gray)

    if not len(faces):
        print("no faces found")
        return
    # print(faces)
    # print(type(faces))
    # print(faces.shape)

    for x, y, w, h in faces:
        pt_1 = (x, y)
        pt_2 = (x + w, y + h)
        # color = (127, 127, 127)
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        thickness = 2
        cv2.rectangle(
            image,
            pt1=pt_1,
            pt2=pt_2,
            color=color,
            thickness=thickness,
        )

    # cv2.imshow("faces", image)
    # cv2.waitKey(0)
    cv2.imwrite("data/image-sm-faces.jpg", image)


if __name__ == "__main__":
    main()

