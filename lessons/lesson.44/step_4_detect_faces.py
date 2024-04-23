import os.path
import random

import cv2 as cv
import numpy as np

CASCADE = "haarcascade_frontalface_default.xml"
face_cascade_path = os.path.join(
    cv.data.haarcascades,
    CASCADE,
)


def main():
    # print(face_cascade_path)
    # print(os.path.isfile(face_cascade_path))
    filename = "data/image-sm.jpg"
    image = cv.imread(filename)
    face_finder = cv.CascadeClassifier(face_cascade_path)
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # faces = face_finder.detectMultiScale(
    #     image_gray,
    #     # scaleFactor=1,
    #     # minSize=(20, 20),
    # )
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


    faces = results[0]
    neighbours = results[1]
    weights = results[2]
    if faces is None or len(faces) == 0:
        print("No faces found")
        return

    # print(faces)
    # print(type(faces))
    assert isinstance(faces, np.ndarray)
    thickness = 2
    for (x, y, w, h), weight in zip(faces, weights):
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
            fontScale=1,
            color=color,
            thickness=thickness,
        )

    # cv.imshow("Image", image)
    cv.imwrite("data/image-sm-faces.jpg", image)


if __name__ == "__main__":
    main()
