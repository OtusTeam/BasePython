import os
import random

import cv2

# f_name = "data/img-cat.jpeg"
f_name = "data/cats.jpg"
CASCADE = "haarcascade_frontalcatface_extended.xml"
# CASCADE = "haarcascade_frontalcatface.xml"

cascade_path = os.path.join(
    cv2.data.haarcascades,
    CASCADE,
)

# print(cascade_path)

def main():
    finder = cv2.CascadeClassifier(cascade_path)

    image = cv2.imread(f_name)
    # print(image.shape)
    image_gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY,
    )
    # print(image_gray.shape)
    # print(image_gray)

    objects = finder.detectMultiScale(image_gray, scaleFactor=5, minSize=(50, 50))

    if not len(objects):
        print("no objects found")
        return
    # print(objects)
    # print(type(objects))
    # print(objects.shape)

    for x, y, w, h in objects:
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

    # cv2.imshow("objects", image)
    # cv2.waitKey(0)
    cv2.imwrite("data/cats-faces-detected.jpg", image)


if __name__ == "__main__":
    main()

