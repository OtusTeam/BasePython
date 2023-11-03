import os.path
import random

import cv2 as cv
import numpy as np

CASCADE = "haarcascade_frontalface_default.xml"

cascade_path = os.path.join(
    cv.data.haarcascades,
    CASCADE,
)


def main():
    filename = "data/image-sm.jpg"
    # filename = "data/img-cat.jpeg"
    # filename = "data/cats.jpg"
    # filename = "data/color-pic-rgb-raw.png"
    image = cv.imread(filename)

    face_finder = cv.CascadeClassifier(cascade_path)
    image_gray = cv.cvtColor(
        image,
        cv.COLOR_BGR2GRAY,
    )
    faces = face_finder.detectMultiScale(image_gray, minSize=(20, 20))

    if faces is None or len(faces) == 0:
        print("no faces found")
        return

    assert isinstance(faces, np.ndarray)
    # print(faces)
    # print(faces.shape)

    for x, y, w, h in faces:
        pt_1 = (x, y)
        pt_2 = (x + w, y + h)

        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        thickness = 2
        cv.rectangle(
            image,
            pt1=pt_1,
            pt2=pt_2,
            color=color,
            thickness=thickness,
        )

        cv.imwrite("data/img-people-faces.jpg", image)


if __name__ == '__main__':
    main()
