

import os
import cv2
import random

RUSSIAN_PLATE_NUMBER = "haarcascade_russian_plate_number.xml"


def main():
    detector = cv2.CascadeClassifier(os.path.join(cv2.data.haarcascades,
                                                  RUSSIAN_PLATE_NUMBER))

    print(detector)

    f_name = 'data/w222-mercedes.jpeg'

    image = cv2.imread(f_name)

    plates: cv2.Mat = detector.detectMultiScale(image)
    print(plates)
    print(type(plates))
    if isinstance(plates, tuple):
        return

    print(plates.shape)
    print(plates.size)
    print("found", len(plates), "plates")
    for x, y, w, h in plates:
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        color = (
            random.
                randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        thickness = -1
        cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("image with pates", image)
    cv2.waitKey(0)
    # cv2.imwrite("data/image-sm_faces.jpg", image)


if __name__ == '__main__':
    main()
