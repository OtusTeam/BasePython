import os
import random

import cv2

f_name = "data/car-plates.jpeg"
CASCADE = "haarcascade_license_plate_rus_16stages.xml"

cascade_path = os.path.join(
    cv2.data.haarcascades,
    CASCADE,
)

# print(cascade_path)

def main():
    plate_finder = cv2.CascadeClassifier(cascade_path)

    image = cv2.imread(f_name)
    # print(image.shape)
    image_gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY,
    )
    # print(image_gray.shape)
    # print(image_gray)

    plates = plate_finder.detectMultiScale(image_gray)

    if not len(plates):
        print("no plates found")
        return
    # print(plates)
    # print(type(plates))
    # print(plates.shape)

    for x, y, w, h in plates:
        pt_1 = (x, y)
        pt_2 = (x + w, y + h)
        # color = (127, 127, 127)
        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
        thickness = 3
        cv2.rectangle(
            image,
            pt1=pt_1,
            pt2=pt_2,
            color=color,
            thickness=thickness,
        )

    # cv2.imshow("plates", image)
    # cv2.waitKey(0)
    cv2.imwrite("data/car-plates-detected.jpg", image)


if __name__ == "__main__":
    main()

