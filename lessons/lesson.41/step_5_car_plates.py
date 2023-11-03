import os.path
import random

import cv2 as cv
import numpy as np

CASCADE = "haarcascade_license_plate_rus_16stages.xml"

cascade_path = os.path.join(
    cv.data.haarcascades,
    CASCADE,
)


def main():
    filename = "data/car-plates.jpeg"
    image = cv.imread(filename)

    face_finder = cv.CascadeClassifier(cascade_path)
    image_gray = cv.cvtColor(
        image,
        cv.COLOR_BGR2GRAY,
    )
    plates = face_finder.detectMultiScale(image_gray)

    if plates is None or len(plates) == 0:
        print("no plates found")
        return

    assert isinstance(plates, np.ndarray)
    # print(plates)
    # print(plates.shape)

    for x, y, w, h in plates:
        pt_1 = (x, y)
        pt_2 = (x + w, y + h)

        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        thickness = 4
        cv.rectangle(
            image,
            pt1=pt_1,
            pt2=pt_2,
            color=color,
            thickness=thickness,
        )

        cv.imwrite("data/img-plates-found.jpeg", image)


if __name__ == '__main__':
    main()
