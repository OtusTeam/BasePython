import os.path
import random

import cv2 as cv


CASCADE = "haarcascade_russian_plate_number.xml"

car_plate_cascade_path = os.path.join(
    cv.data.haarcascades,
    CASCADE,
)


def main():
    image_filepath = "data/car-plates.jpeg"
    img = cv.imread(image_filepath)

    plate_finder = cv.CascadeClassifier(car_plate_cascade_path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    result = plate_finder.detectMultiScale3(
        img_gray,
        scaleFactor=1.1,
        # minNeighbors=5,
        # minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE,
        outputRejectLevels=True
    )
    plates, neighbours, weights = result

    if plates is None or len(plates) == 0:
        print("No results found")
        return

    print(plates)
    print("plates count:", len(plates))

    for (x, y, w, h), weight in zip(plates, weights):
        pt_1 = x, y
        pt_2 = x + w, y + h
        color = tuple(
            random.randint(0, 255)
            for _ in range(3)
        )

        thickness = 2
        cv.rectangle(
            img=img,
            pt1=pt_1,
            pt2=pt_2,
            thickness=thickness,
            color=color,
        )
        cv.putText(
            img=img,
            text=str(round(weight, 2)),
            org=(x, y - 3),
            fontFace=cv.FONT_HERSHEY_PLAIN,
            fontScale=2,
            color=color,
            thickness=thickness,

        )

    # TODO: read plate w/ OCR (Optical character recognition)

    # cv.imshow("Image", img)
    cv.imwrite("data/car-license-plates.jpeg", img)



if __name__ == "__main__":
    main()
