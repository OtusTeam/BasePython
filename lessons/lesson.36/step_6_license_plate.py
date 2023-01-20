import os
from random import randint

import cv2

file_name = "data/car-plates.jpeg"

cascade_file_license_plate = "haarcascade_russian_plate_number.xml"
CASCADE_PATH = os.path.join(cv2.data.haarcascades, cascade_file_license_plate)

detector = cv2.CascadeClassifier(CASCADE_PATH)


def main():
    image = cv2.imread(file_name)
    if image is None:
        print("could not read image")
        return

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    scale_factor = 1.2
    neighbours = 3
    boxes = detector.detectMultiScale(
        image_gray,
        scale_factor,
        neighbours,
    )
    print(boxes)

    if boxes is not None:
        for x, y, w, h in boxes:
            p1 = x, y
            p2 = x + w, y + h
            color = (
                randint(0, 255),
                randint(0, 255),
                randint(0, 255),
            )

            thickness = 2
            cv2.rectangle(image, p1, p2, color, thickness)

    cv2.imshow("plates", image)
    cv2.waitKey(0)

    # cv2.imwrite("data/out/kittens-sm.jpg", image)


if __name__ == "__main__":
    main()
