import os.path
import random

import cv2 as cv


CASCADE = "haarcascade_frontalface_default.xml"

face_cascade_path = os.path.join(
    cv.data.haarcascades,
    CASCADE,
)


def main():
    image_filepath = "data/image-sm.jpg"
    img = cv.imread(image_filepath)

    face_finder = cv.CascadeClassifier(face_cascade_path)
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # faces = face_finder.detectMultiScale(
    result = face_finder.detectMultiScale3(
        img_gray,
        # img,
        scaleFactor=1.1,
        # minNeighbors=5,
        # minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE,
        outputRejectLevels=True
    )
    faces, neighbours, weights = result

    if faces is None or len(faces) == 0:
        print("No results found")
        return

    print(faces)
    print("faces count:", len(faces))

    for (x, y, w, h), weight in zip(faces, weights):
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

    # cv.imshow("Image", img)
    cv.imwrite("data/image-sm-faces.jpg", img)



if __name__ == "__main__":
    main()
