import os
from random import randint

import cv2

# file_name = "data/kittens.jpg"
file_name = "data/image-sm.jpg"

cascade_file_frontal_face = "haarcascade_frontalface_default.xml"
CASCADE_PATH = os.path.join(cv2.data.haarcascades, cascade_file_frontal_face)

detector = cv2.CascadeClassifier(CASCADE_PATH)


def main():
    image = cv2.imread(file_name)
    if image is None:
        print("could not read image")
        return

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # image_h, image_w = image.shape

    # image_h, image_w, _ = image.shape
    # scale = 1

    # target_d = int(image_w * scale), int(image_h * scale)
    # # image_sm = cv2.resize(image, target_d)
    # image_sm = image

    scale_factor = 1.05
    neighbours = 4
    faces = detector.detectMultiScale(
        image_gray,
        scale_factor,
        neighbours,
        minSize=(30, 30),
    )
    print(faces)

    if faces is not None:
        for x, y, w, h in faces:
            p1 = x, y
            p2 = x + w, y + h
            # color = (150, 50, 250)
            color = (
                randint(0, 255),
                randint(0, 255),
                randint(0, 255),
            )

            thickness = 2
            cv2.rectangle(image, p1, p2, color, thickness)

    cv2.imshow("faces", image)
    cv2.waitKey(0)

    # cv2.imwrite("data/out/kittens-sm.jpg", image)


if __name__ == "__main__":
    main()
