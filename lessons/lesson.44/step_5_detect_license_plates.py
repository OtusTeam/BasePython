import os.path
import random

import cv2 as cv
import numpy as np

CASCADE = "haarcascade_russian_plate_number.xml"
license_plate_cascade_path = os.path.join(
    cv.data.haarcascades,
    CASCADE,
)


def main():
    filename = "data/car-plates.jpeg"
    image = cv.imread(filename)
    face_finder = cv.CascadeClassifier(license_plate_cascade_path)
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    results = face_finder.detectMultiScale3(
        image_gray,
        # scaleFactor=1,
        # minSize=(20, 20),
        flags=cv.CASCADE_SCALE_IMAGE,
        outputRejectLevels=True
    )
    if results is None or len(results) == 0:
        print("No results found")
        return

    plates = results[0]
    # neighbours = results[1]
    weights = results[2]
    if plates is None or len(plates) == 0:
        print("No plates found")
        return

    assert isinstance(plates, np.ndarray)
    thickness = 3
    font_thickness = 2
    font_scale = 2
    for (x, y, w, h), weight in zip(plates, weights):
        pt_1 = (x, y)
        pt_2 = (x + w, y + h)
        color = tuple(
            random.randint(0, 255) for _ in range(3)
        )
        cv.rectangle(
            img=image,
            pt1=pt_1,
            pt2=pt_2,
            thickness=thickness,
            color=color,
        )
        cv.putText(
            img=image,
            text=str(round(weight, 2)),
            org=(x, y),
            fontFace=cv.FONT_HERSHEY_SIMPLEX,
            fontScale=font_scale,
            color=color,
            thickness=font_thickness,
        )

    # cv.imshow("Image", image)
    cv.imwrite("data/car-plates-frames.jpeg", image)


if __name__ == "__main__":
    main()
